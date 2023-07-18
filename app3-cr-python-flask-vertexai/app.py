from flask import Flask, render_template, request, jsonify
import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair


app = Flask(__name__)
PROJECT_ID = "$PROJECT_ID" #Your Google Cloud Project ID
LOCATION = "us-central1"              #us-central1 for now
vertexai.init(project=PROJECT_ID, location=LOCATION)


def create_session():
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    chat = chat_model.start_chat()
    return chat

def response(chat, message):
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40
    }
    response = chat.send_message(message, **parameters)
    return response.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/palm2', methods=['GET', 'POST'])
def vertexPalM():
    user_input = request.args.get('user_input') if request.method == 'GET' else request.form['user_input']
    chat_model = create_session()
    content = response(chat_model,user_input)

    return jsonify(content=content)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
