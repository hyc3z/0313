from revChatGPT.V1 import Chatbot
import os
session_token = os.environ.get('SESSION_TOKEN')
chatbot = Chatbot(config = {
    "session_token": session_token
})
from flask import Flask, request

app = Flask(__name__)
@app.route('/chat', methods = ['POST'])
def hello_world():
    return_message = ""
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        # you can use <user_id>, which is a str but could
        # changed to be int or whatever you want, along
        # with your lxml knowledge to make the required
        # changes
        input_data = request.get_data().decode('utf-8')
        prev_text = ""
        for data in chatbot.ask(
            input_data,
        ):
            message = data["message"][len(prev_text) :]
            return_message += message
            prev_text = data["message"]
        return return_message

if __name__ == "__main__":
    app.run()