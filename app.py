from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def predict(text):
    return model(text)[0]['summary_text']

with gr.Blocks() as demo:
    textbox = gr.Textbox(placeholder="Enter text block to summarize", lines=4)
    gr.Interface(fn=predict, inputs=textbox, outputs="text")

demo.launch()