import os
import json
import functions_framework
import google.cloud.logging
from langchain.llms.vertexai import VertexAI

PROJECT_ID  = os.environ.get('GCP_PROJECT','-')
LOCATION = os.environ.get('GCP_REGION','-')

client = google.cloud.logging.Client(project=PROJECT_ID)
client.setup_logging()

log_name = "predictText-cloudfunction-log"
logger = client.logger(log_name)

@functions_framework.http
def predictText(request):

    request_json = request.get_json(silent=True)

    if request_json and 'prompt' in request_json:
        prompt = request_json['prompt']
        logger.log(f"Received request for prompt: {prompt}")
        llm = VertexAI(project=PROJECT_ID, location=LOCATION)
        prompt_response = llm(prompt)
        logger.log(f"PaLM Text Bison Model response: {prompt_response}")
    else:
        prompt_response = 'No prompt provided.'

    return json.dumps({"response_text":prompt_response})
