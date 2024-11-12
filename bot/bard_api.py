import google.generativeai as genai
from config import BARD_API_KEY

genai.configure(api_key=BARD_API_KEY)

def bard_generate(text):
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content(text)
    return response.text
