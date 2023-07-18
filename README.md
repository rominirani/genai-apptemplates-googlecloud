# Gen AI on Google Cloud Workshop
The goal of this repository is to provide a list of applications that you can deploy on Google Cloud. The applications demonstrate how you can use standard frameworks like Python Flask, Streamlit, Gradio to host applications on Google Cloud that interact with the Vertex AI PaLM Models : Text , Chat and Code. 

These code samples are provided as templates that you can use while creating a New Application via [Cloud Code Visual Studio](https://cloud.google.com/code) plugin. Official instructions are provided [here](https://cloud.google.com/code/docs/vscode/set-up-sample-repo).

## Custom Samples Configuration File (.cctemplate)
The key thing to understand is the presence of the `.cctemplate` file in this repo. It contains the `templates` element that has entries for the two folders or samples that you have in this repository:
- `java-springboot-api`
- `python-flask-api`

```
{
   "metadata":{
      "version":"1"
   },
   "name": "Sample Applications deployable on Google Cloud that demonstrate Vertex AI Generative AI usage",
   "templates":[
      {
         "path":"app1-cf-python-vertexai-http",
         "name":"App 1 : Python Cloud Function",
         "description":"Python Cloud Function invoking PaLM API Models via Vertex AI API"
      },
       {
         "path":"app2-cf-python-vertexai-gcs",
         "name":"App 2 : Python Cloud Function processing GCS documents",
         "description":"Python Cloud Function that invokes summarization with PaLM API Models via Vertex AI API on GCS documents"
      }
       {
         "path":"app3-cr-python-flask-vertexai",
         "name":"App 3 : Python Flask-based Web Chat Application",
         "description":"Cloud Run application with Web UI that demonstrates working with Vertex AI API"
      }
       {
         "path":"app4-cr-python-gradio-vertexai",
         "name":"App 4 : Gradio Web Application interacting with PaLM Model via VerteX AI API",
         "description":"Cloud Run application utilizing Gradio Framework that demonstrates working with Vertex AI API"
      }
       {
         "path":"app5-cr-python-streamlit-vertexai",
         "name":"App 5 : Streamlit Web Application interacting with PaLM Model via VerteX AI API",
         "description":"Cloud Run application utilizing Streamlit Framework that demonstrates working with Vertex AI API"
      }
   ]
}
```

## What are the sample applications about?
You can go through the various projects and pick a project or two that interests you. Refer to the description for each of the projects above. The repository provides a mix of examples that help you pick a combination of one or more of Cloud Functions, Cloud Run, Streamlit, Gradio and Flask frameworks.


## Using the Custom Samples via Cloud Code plugin

1. Assuming that you have Visual Studio Code and the Cloud Code plugin setup, click on the Cloud Code link in the status bar.
2. Click on `New Application`
3. Select `Custom Application`
4. When asked for the Git Repository URL, enter the URL of this repository: `https://github.com/rominirani/cloud-code-sample-repository.git`
5. You will shown all the projects. Select one of your choice.
6. Complete the rest of the steps to import the projects into Visual Studio Code.

## Deploying the application(s) on Google Cloud
You can choose to use Cloud Code VS Extension itself to deploy any of these applications to Google Cloud in your specific Cloud Project and Account. Alternately, feel free to use the console and /or `gcloud` commands to deploy the same. 
