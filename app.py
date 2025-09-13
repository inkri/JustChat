import gradio as gr
from agent_app import ask  # your existing FastAPI function

def query_api(prompt):
    result = ask({"prompt": prompt})  # call your function directly
    return result["answer"]

iface = gr.Interface(
    fn=query_api,
    inputs="text",
    outputs="text",
    title="LLM Agent API",
    description="Ask questions to the model."
)

iface.launch()