from flask import Flask, render_template, request
from gemini_chat import get_gemini_response

app = Flask(__name__)

# Home route to show the form (GET)
@app.route("/", methods=["GET"])
def home():
    # Default response when no input is given (optional)
    default_response = {
        "metadata": {
            "query": "",
            "language": "English",
            "generated_at": "2025-08-07T12:34:00",
            "model_version": "GPT-4.5"
        },
        "data": {
            "title": "Welcome to BheemGPT",
            "summary": "Ask me anything, and I'll try to help!",
            "details": []
        }
    }
    return render_template("index.html", response=default_response)

# POST route to handle form submission (for new prompts)
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form.get("prompt")
    response_text = get_gemini_response(user_input)

    # Structure the response for rendering, ensuring 'data' is present
    response_data = {
        "metadata": {
            "query": user_input,
            "language": "English",
            "generated_at": "2025-08-07T12:34:00",  # You can dynamically generate the timestamp
            "model_version": "GPT-4.5"
        },
        "data": {  # Wrap your current data under 'data'
            "title": "Gemini GPT",
            "summary": response_text,
            "details": []
        }
    }

    # You can add more specific details based on the response content
    if "example" in response_text.lower():
        response_data["data"]["details"].append({
            "section": "Example Explanation",
            "description": "This is an example explanation to further clarify the concept.",
            "code": "```python\nprint('Hello, World!')\n```",
            "bullets": [
                "Point 1: This is the first bullet point explaining the example.",
                "Point 2: This is the second bullet point explaining further."
            ]
        })

    return render_template("index.html", user_input=user_input, response=response_data)

if __name__ == "__main__":
    app.run(debug=True)
