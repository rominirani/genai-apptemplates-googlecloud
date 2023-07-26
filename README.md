# Gen AI Application templates on Google Cloud
The goal of this repository is to provide a list of applications that you can deploy on Google Cloud. The applications demonstrate how you can use standard frameworks like Python Flask, Streamlit, Gradio to host applications on Google Cloud that interact with the Vertex AI PaLM Models : Text , Chat and Code. These code samples are provided as templates that you can use. You can go through the various projects and pick a project or two that interests you. Click on any of the projects to see detailed documentation, sample template and instructions to deploy on Google Cloud. 

## List of Applications 
- [App 1 : Python Cloud Function that invokes the Text and Code PaLM Models](app1-cf-python-vertexai-http)
- [App 2 : Python Cloud Function processing GCS documents and summarizes the contents via the Text PaLM Model](app2-cf-python-vertexai-gcs)
- [App 3 : Python Flask-based Web Chat Application that integrates with Chat PaLM Model](app3-cr-python-flask-vertexai)
- [App 4 : Gradio Web Application interacting with PaLM Model via VerteX AI API](app4-cr-python-gradio-vertexai)
- [App 5 : Streamlit Web Application interacting with PaLM Model via VerteX AI API](app5-cr-python-streamlit-vertexai)

## Using the Custom Samples via Cloud Code plugin

1. Assuming that you have Visual Studio Code and the Cloud Code plugin setup, click on the Cloud Code link in the status bar.
2. Click on `New Application`
3. Select `Custom Application`
4. When asked for the Git Repository URL, enter the URL of this repository: `https://github.com/rominirani/cloud-code-sample-repository.git`
5. You will shown all the projects. Select one of your choice.
6. Complete the rest of the steps to import the projects into Visual Studio Code.

Check the screencast below:
<img src="import-apps-into-cloudcode.gif"/>

## Deploying the application(s) on Google Cloud
You can choose to use Cloud Code VS Extension itself to deploy any of these applications to Google Cloud in your specific Cloud Project and Account. Alternately, feel free to use the console and /or `gcloud` commands to deploy the same. Please visit each of the folders for the respective instructions to deploy to Google Cloud. 

This is not an official Google Cloud Project.
