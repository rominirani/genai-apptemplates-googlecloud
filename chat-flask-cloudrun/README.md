# Cloud Run application with Web UI that demonstrates working with Vertex AI API

This application demonstrates a Cloud Run application that has a simple Form-based UI that represents a Chat widget. You can put in your query and it will invoke the PaLM Chat Bison model in the background and get back the response. It is a simple example but something that you can look to embed into your larger web application.

![Flask Chat App Screen](../images/flaskapp-screen.png "Flask Chat App")

## Build and Deploy the application to Cloud Run

To deploy the Flask Application in [Cloud Run](https://cloud.google.com/run/docs/quickstarts/deploy-container), you need to build the Docker image in Artifact Registry and deploy it in Cloud Run.

First step is to add your Google Project ID in the `app.py` file.

Next, look at the following script, replace the variables at the start and run the commands one after the other. This assumes that you have `gcloud` setup on your machine.

```sh
PROJECT_ID=<REPLACE_WITH_YOUR_PROJECT_ID>
REGION=<REPLACE_WITH_YOUR_GCP_REGION_NAME>
AR_REPO=<REPLACE_WITH_YOUR_AR_REPO_NAME>
SERVICE_NAME=chat-flask-app
gcloud artifacts repositories create $AR_REPO --location=$REGION --repository-format=Docker
gcloud auth configure-docker $REGION-docker.pkg.dev
gcloud builds submit --tag $REGION-docker.pkg.dev/$PROJECT_ID/$AR_REPO/$SERVICE_NAME
gcloud run deploy $SERVICE_NAME --port 8080 --image $REGION-docker.pkg.dev/$PROJECT_ID/$AR_REPO/$SERVICE_NAME --allow-unauthenticated --region=$REGION --platform=managed  --project=$PROJECT_ID
```

