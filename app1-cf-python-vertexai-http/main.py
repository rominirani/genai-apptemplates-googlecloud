import functions_framework
import os

from google.cloud import aiplatform
import google.cloud.logging

import vertexai
from vertexai.language_models import TextGenerationModel
from vertexai.preview.language_models import CodeGenerationModel

PROJECT_ID  = os.environ.get('GCP_PROJECT','-')
LOCATION = os.environ.get('FUNCTION_REGION','-')

client = google.cloud.logging.Client(project=PROJECT_ID)
client.setup_logging()

log_name = "genai-cloudfunction-log"
logger = client.logger(log_name)

models = ["code","text"]

def predictText(prompt, max_output_tokens, temperature, top_p, top_k):
    vertexai.init(project=PROJECT_ID, location=LOCATION)
    model = TextGenerationModel.from_pretrained("text-bison@001")
    answer = model.predict(
        prompt,
        max_output_tokens=max_output_tokens, # default 128
        temperature=temperature, # default 0
        top_p=top_p, # default 1
        top_k=top_k) # default 40
    logger.log("PaLM Text Bison Model response: {}".format(answer))    
    return answer

def predictCode(prompt, max_output_tokens, temperature):
    vertexai.init(project=PROJECT_ID, location=LOCATION)
    model = CodeGenerationModel.from_pretrained("code-bison@001")
    answer = model.predict(
        prompt,
        max_output_tokens=max_output_tokens, # default 128
        temperature=temperature) # default 0
    logger.log("PaLM Code Bison Model response: {}".format(answer))    
    return answer

@functions_framework.http
def predict(request):

    request_json = request.get_json(silent=True)
    request_args = request.args

    model_requested = request_args.get("model","text")
    if model_requested not in models:
        model_requested="text"
    logger.log("Model Requested: {}".format(model_requested))
    if request_json and 'prompt' in request_json:
        prompt = request_json['prompt']
        logger.log("Received request for prompt: {}".format(prompt))
        if model_requested == "text":
            prompt_response = predictText(prompt,512,0.2,0.8,38)
        elif model_requested == "code":
            prompt_response = predictCode(prompt,1024,0.2)
    else:
        prompt_response = 'No prompt provided.'

    return "Response: {}".format(prompt_response)
