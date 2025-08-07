import google.generativeai as genai
from config import API_KEY

# Configure the Gemini API
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")
chat = model.start_chat(history=[])

# Function to get response
def get_gemini_response(user_input):
    try:
        response = chat.send_message(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
