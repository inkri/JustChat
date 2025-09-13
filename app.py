import gradio as gr
from agent_app import handle_user_input, AgentState, app_graph

def query_api(prompt: str) -> str:
    # Use the compiled LangGraph flow to handle the query
    final_state = app_graph.invoke({"user_input": prompt})
    return final_state["response"]

# Gradio interface
iface = gr.Interface(
    fn=query_api,
    inputs=gr.Textbox(lines=2, placeholder="Ask me anything..."),
    outputs="text",
    title="JustChat LLM Agent",
    description="Ask questions to the model. Uses TinyLlama + RAG + Web Search."
)

iface.launch()
