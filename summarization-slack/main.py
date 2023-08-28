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
log_name = "slack-summarizeText-cloudfunction-log"
logger = client.logger(log_name)


@functions_framework.http
def summarizeText(request):
    token = request.form['token']
    logger.log(f"token received = {token}")
    #<TODO>Your code to validate token
    
    request_text = request.form['text']
    logger.log(f"Received the following request to summarize : {request_text}")

    vertexai.init(project=PROJECT_ID, location=LOCATION)
    model = TextGenerationModel.from_pretrained("text-bison@001")
    prompt = f"Summarize: {request_text}"
    parameters = {
       "temperature": 0.2,
       "max_output_tokens": 256,
       "top_p": 0.8,
       "top_k": 40
    }
    prompt_response = model.predict(prompt,**parameters)
    logger.log("PaLM Text Bison Model response: {prompt_response.text}")

    #Format the Slack message
    data = {}
    data['blocks'] = []
    data['blocks'].append({"type":"section",
                     "text": {
				            "type": "mrkdwn",
				            "text": "Your message: " + request_text + "\n>Summarization:" + prompt_response.text
			            }
                    })
    return json.dumps(data),200, {'Content-Type': 'application/json'}

