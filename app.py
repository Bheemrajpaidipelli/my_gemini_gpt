from flask import Flask, render_template, request
from gemini_chat import GeminiChat

API_KEY = "AIzaSyDi1VGs1vi-iFEMYqF1Li0IEltI3SPMfhY" 

app = Flask(__name__)
chatbot = GeminiChat(api_key=API_KEY)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = chatbot.get_response(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
