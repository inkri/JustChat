from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langgraph.graph import StateGraph, END
from typing import TypedDict
from datasets import load_dataset
from duckduckgo_search import ddg

# -----------------------
# Model setup (TinyLlama)
# -----------------------
MODEL_DIR = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForCausalLM.from_pretrained(MODEL_DIR, device_map="auto")

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=512,
    do_sample=True,
    temperature=0.7,
)

# -----------------------
# Load dataset (SQuAD subset)
# -----------------------
dataset = load_dataset("squad", split="train[:500]")  # small subset for speed
DATA_KB = []
for item in dataset:
    context = item.get("context", "")
    question = item.get("question", "")
    answers = item.get("answers", {}).get("text", [])
    DATA_KB.append((context, question, answers))

# -----------------------
# LangGraph state
# -----------------------
class AgentState(TypedDict):
    user_input: str
    response: str

# -----------------------
# Tools
# -----------------------
def rag_tool(query: str) -> str:
    """Search in dataset KB"""
    for context, question, answers in DATA_KB:
        if query.lower() in question.lower() or query.lower() in context.lower():
            return f"Context: {context}\nAnswer: {answers[0] if answers else 'No answer'}"
    return "No relevant info found in KB."

def web_search_tool(query: str) -> str:
    """Search DuckDuckGo and return first 3 results"""
    results = ddg(query, max_results=3)
    if results:
        return "\n".join([r.get("body", r.get("title", "")) for r in results[:3]])
    return "No results found online."

# -----------------------
# Handle user input
# -----------------------
def handle_user_input(state: AgentState) -> AgentState:
    query = state["user_input"]

    # Check KB first (RAG)
    kb_result = rag_tool(query)
    if "No relevant info" not in kb_result:
        response = f"[RAG KB Result]\n{kb_result}"
    else:
        # Fallback to DuckDuckGo search
        search_result = web_search_tool(query)
        response = f"[Web Search Result]\n{search_result}"

    # Generate LLM response
    prompt = f"[INST] {query} [/INST]\nAdditional info:\n{response}"
    out = generator(prompt, max_new_tokens=200)
    state["response"] = out[0]["generated_text"]
    return state

# -----------------------
# LangGraph flow
# -----------------------
graph = StateGraph(AgentState)
graph.add_node("HANDLE_INPUT", handle_user_input)
graph.set_entry_point("HANDLE_INPUT")
graph.add_edge("HANDLE_INPUT", END)
app_graph = graph.compile()

# -----------------------
# Function to call from Gradio
# -----------------------
def ask(prompt: str) -> str:
    final_state = app_graph.invoke({"user_input": prompt})
    return final_state["response"]
