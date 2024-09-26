import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def get_embeddings(text):
    url = 'https://api.openai.com/v1/embeddings'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + os.getenv("OPENAI_API_KEY")
    }

    data = {
        'input': text,
        'model': 'text-embedding-ada-002',
        'options': { 'wait_for_model': True }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    responseData = response.json()

    return responseData['data'][0]['embedding']

