import json
import ast

from revChatGPT.V1 import Chatbot
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://bob.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("OPENAI_API_KEY")
ALLOWED_KEYS = os.getenv("APP_ALLOWED_KEYS")

from flask import Flask, request, Response

system_message_template = "<|im_start|>system\n{}\n<|im_end|>"
system_message = system_message_template.format("")

def create_prompt(system_message, messages):
    prompt = system_message
    message_template = "\n<|im_start|>{}\n{}\n<|im_end|>"
    for message in messages:
        prompt += message_template.format(message['sender'], message['text'])
    prompt += "\n<|im_start|>assistant\n"
    return prompt

# messages = [{"sender": "user", "text": "USER_INPUT_GOES_HERE"}]

app = Flask(__name__)
@app.route('/chat', methods = ['POST'])
def track():
    return_message = ""
    if request.method == 'POST':
        try:
            allowed_keys = ast.literal_eval(ALLOWED_KEYS)
            token = request.headers.get('Authorization').replace("Bearer ", "")
            if token not in allowed_keys:
                return Response(
                    "Request invalid. Invalid authorization token.",
                    status=401,
                )
            input_data = request.get_data(as_text=True)
            # List of messages
            messages = json.loads(input_data)
            response = openai.Completion.create(
                engine="Agda",
                prompt= create_prompt(system_message_template.format(input_data), messages),
                temperature=0.19,
                max_tokens=4000,
                top_p=0.06,
                frequency_penalty=0,
                presence_penalty=0,
                stop=["<|im_end|>"])
            return response
        except Exception as e:
            return Response(
                "Request invalid. {}".format(e.message),
                status=400,
            )

if __name__ == "__main__":
    app.run()