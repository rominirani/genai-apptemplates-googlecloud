import os
import json
import functions_framework

import google.cloud.logging

import vertexai
from vertexai.language_models import TextGenerationModel

PROJECT_ID  = os.environ.get('GCP_PROJECT','-')
LOCATION = os.environ.get('GCP_REGION','-')
client = google.cloud.logging.Client(project=PROJECT_ID)
client.setup_logging()
log_name = "wotd-cloudfunction-log"
logger = client.logger(log_name)


@functions_framework.http
def wotd(request):
    logger.log(f"Received a request for Word of the Day")

    vertexai.init(project=PROJECT_ID, location=LOCATION)
    model = TextGenerationModel.from_pretrained("text-bison@001")
    prompt = f"Provide a random word in English with its explanation and example usage."
    parameters = {
       "temperature": 1.0,
       "max_output_tokens": 256,
       "top_p": 1.0,
       "top_k": 40
    }
    prompt_response = model.predict(prompt,**parameters)
    logger.log("PaLM Text Bison Model response: {prompt_response.text}")

    #Format the response
    data = {}
    data['wotd'] = []
    data['wotd'].append({"details": prompt_response.text})
    return json.dumps(data),200, {'Content-Type': 'application/json'}

