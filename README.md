# Sample Apps built with various different tools utilising Vertex PaLM API

Sample Applications have been provided that you can deploy on Google Cloud. 


The applications demonstrate how you can use standard frameworks like Python Flask, Streamlit, Gradio to host applications on Google Cloud that interact with the Vertex AI PaLM Models : Text , Chat and Code. 

These code samples are provided as templates that you can use. You can go through the various projects and pick a project or two that interests you. Click on any of the projects to see detailed documentation, sample template and instructions to deploy on Google Cloud.

## Sample Applications

| Application Name | Description | Technologies Used |
|---|---|---|
|[chat-flask-cloudrun](chat-flask-cloudrun)|Python Flask-based Web Chat Application interacting with Vertex AI Chat PaLM Model.|Cloud Run, Python Flask|
|[chat-gradio](chat-gradio)|Gradio Web Application interacting with Vertex AI Text PaLM Model.|Cloud Run, Gradio, Python|
|[chat-streamlit](chat-streamlit)|Streamlit Web Application interacting with Vertex AI Text PaLM Model.|Cloud Run, Streamlit, Python|
|[code-predict-cloudfunction](code-predict-cloudfunction)|Python Cloud Function that invokes the Vertex AI Text PaLM Model.|Cloud Functions v2, Python|
|[text-predict-cloudfunction](text-predict-cloudfunction)|Python Cloud Function that invokes the Vertex AI Code PaLM Model.|Cloud Functions v2, Python|
|[summarization-gcs-cloudfunction](summarization-gcs-cloudfunction)|Python Cloud Function processing Cloud Storage documents and summarizes the contents via the Vertex AI Text PaLM Model. |Cloud Functions v2, Cloud Storage, Python|

## Environment Setup

Before you run any of the above applications, ensure that you have followed the instructions in [SETUP.md](SETUP.md).
