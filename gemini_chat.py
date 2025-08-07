import google.generativeai as genai

class GeminiChat:
    def __init__(self, api_key, model_name="models/gemini-2.5-pro"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name=model_name)
        self.chat = self.model.start_chat(history=[])

    def get_response(self, user_input):
        try:
            response = self.chat.send_message(user_input)
            return response.text
        except Exception as e:
            return f"Error: {e}"
