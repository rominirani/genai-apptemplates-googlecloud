# Sample Apps built with various different tools utilising Vertex PaLM API

Sample Applications have been provided that you can deploy on Google Cloud. 

The applications demonstrate how you can use standard frameworks like Python Flask, Streamlit, Gradio to host applications on Google Cloud that interact with the Vertex AI PaLM Models : Text , Chat and Code. 

These code samples are provided as templates that you can use. You can go through the various projects and pick a project or two that interests you. Click on any of the projects to see detailed documentation, sample template and instructions to deploy on Google Cloud.

## Environment Setup

Before you run any of the sample applications, ensure that you have followed the instructions in [SETUP.md](SETUP.md).

## Sample Applications

| Application Name | Description | Technologies Used |
|---|---|---|
|[chat-flask-cloudrun](chat-flask-cloudrun)|Python Flask-based Web Chat Application interacting with Vertex AI Chat PaLM Model.|Cloud Run, Python Flask|
|[chat-gradio](chat-gradio)|Gradio Web Application interacting with Vertex AI Text PaLM Model.|Cloud Run, Gradio, Python|
|[chat-streamlit](chat-streamlit)|Streamlit Web Application interacting with Vertex AI Text PaLM Model.|Cloud Run, Streamlit, Python|
|[code-predict-cloudfunction](code-predict-cloudfunction)|Python Cloud Function that invokes the Vertex AI Text PaLM Model.|Cloud Functions v2, Python|
|[text-predict-cloudfunction](text-predict-cloudfunction)|Python Cloud Function that invokes the Vertex AI Code PaLM Model.|Cloud Functions v2, Python|
|[summarization-gcs-cloudfunction](summarization-gcs-cloudfunction)|Python Cloud Function processing Cloud Storage documents and summarizes the contents via the Vertex AI Text PaLM Model. |Cloud Functions v2, Cloud Storage, Python|

## Using the Custom Samples via Cloud Code plugin

Assuming that you have Visual Studio Code and the Cloud Code plugin setup, click on the Cloud Code link in the status bar.
- Click on New Application
- Select Custom Application
- When asked for the Git Repository URL, enter the URL of this repository: https://github.com/rominirani/genai-apptemplates-googlecloud
- You will shown all the projects. Select one of your choice.
- Complete the rest of the steps to import the projects into Visual Studio Code.

Check the screencast below:
<img src="import-apps-into-cloudcode.gif"/>
