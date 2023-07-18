# Cloud Run application utilizing Gradio Framework that demonstrates working with Vertex AI API

This application demonstrates a Cloud Run application that uses the [Gradio](https://www.gradio.app/) framework. This project is inspired/taken from the following repository: [https://github.com/rafaelsf80/genai-vertex-text](https://github.com/rafaelsf80/genai-vertex-text).

## User managed service account for Cloud Run

Since the application is deployed in Cloud Run, it uses the permissions of the compute service account by default. In this application, we can look at a best practice to use a separate service account for minimum permissions. To do that, [create the service account with impersonation](https://cloud.google.com/run/docs/securing/service-identity) and the following two extra roles: `roles/aiplatform.user` to be able to call predictions and `roles/logging.logWriter` to be able to write logs.

```sh
PROJECT_ID=<REPLACE_WITH_YOUR_PROJECT_ID>
USER_ACCOUNT=<REPLACE_WITH_YOUR_USER_ACCOUNT>
# Create service account
gcloud iam service-accounts create cloud-run-llm \
    --description="Service account to call LLM models from Cloud Run" \
    --display-name="cloud-run-llm"

# add aiplatform.user role
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:cloud-run-llm@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/aiplatform.user"

# add logging.logWriter role
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:cloud-run-llm@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/logging.logWriter"

# add permission to impersonate the sa (iam.serviceAccounts.actAs), since this is a user-namaged sa
gcloud iam service-accounts add-iam-policy-binding \
    cloud-run-llm@$PROJECT_ID.iam.gserviceaccount.com \
    --member="user:$USER_ACCOUNT" \
    --role="roles/iam.serviceAccountUser"
```

## Build and deploy in Cloud Run

To build and deploy the [Gradio app](https://gradio.app/) in [Cloud Run](https://cloud.google.com/run/docs/quickstarts/deploy-container), you need to build the Docker image in Artifact Registry and deploy it in Cloud Run.

Note authentication is disabled and the service account is the one configured earlier:

```sh
PROJECT_ID=<REPLACE_WITH_YOUR_PROJECT_ID>
REGION=<REPLACE_WITH_YOUR_GCP_REGION_NAME>
AR_REPO=<REPLACE_WITH_YOUR_AR_REPO_NAME>
SERVICE_NAME=genai-text-demo
gcloud artifacts repositories create $AR_REPO --location=$REGION --repository-format=Docker
gcloud auth configure-docker $REGION-docker.pkg.dev
gcloud builds submit --tag $REGION-docker.pkg.dev/$PROJECT_ID/$AR_REPO/$SERVICE_NAME
gcloud run deploy $SERVICE_NAME --port 7860 --image $REGION-docker.pkg.dev/$PROJECT_ID/$AR_REPO/$SERVICE_NAME --service-account=cloud-run-llm@$PROJECT_ID.iam.gserviceaccount.com --allow-unauthenticated --region=$REGION --platform=managed  --project=$PROJECT_ID
```
