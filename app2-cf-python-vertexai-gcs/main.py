import functions_framework
from google.cloud import storage
import os

from google.cloud import aiplatform

import vertexai
from vertexai.language_models import TextGenerationModel
from vertexai.preview.language_models import CodeGenerationModel

PROJECT_ID  = os.environ.get('GCP_PROJECT','-')
LOCATION = os.environ.get('FUNCTION_REGION','-')

def predictText(prompt, max_output_tokens, temperature, top_p, top_k):
    vertexai.init(project=PROJECT_ID, location=LOCATION)
    model = TextGenerationModel.from_pretrained("text-bison@001")
    answer = model.predict(
        prompt,
        max_output_tokens=max_output_tokens, # default 128
        temperature=temperature, # default 0
        top_p=top_p, # default 1
        top_k=top_k) # default 40
    return str(answer)

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data


    bucketname = data["bucket"]
    name = data["name"]

    # Read the contents of the blob
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucketname)
    blob = bucket.blob(name)

    file_contents = blob.download_as_text(encoding="utf-8")

    # Invoke the predict function with the Summarize prompt
    prompt = "Summarize the following: {}".format(file_contents)
    prompt_response = predictText(prompt,1024,0.2,0.8,38)
    print(prompt_response)

    # Save the summary in another blob in the summary bucket
    split_names = name.split(".")
    summary_blob_name = "{}-summary.{}".format(split_names[0],split_names[1])
    summarization_bucket = storage_client.bucket("{}-summaries".format(bucketname))
    summary_blob = summarization_bucket.blob(summary_blob_name)
    summary_blob.upload_from_string(prompt_response.encode('utf-8'))
    print("Summarization saved in {}/{}".format(summarization_bucket))
