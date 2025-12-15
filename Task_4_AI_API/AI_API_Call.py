import requests
import os

# API key should be stored in env variable
API_KEY = os.getenv("OPENAI_API_KEY")

URL="https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization":f"Bearer {API_KEY}",
    "Content-Type":"application/json"
}

payload = {
    "model": "gpt-3.5-turbo",
    "messages":[
        {"role":"user","content":"Explain Artificial Intelligence in simple terms"}
    ]
}

try:
    response=requests.post(URL,headers=headers,json=payload)
    response.raise_for_status()

    result=response.json()
    output_text=result["choices"][0]["message"]["content"]

    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(output_text)

    print("response saved to output.txt")

except Exception as error:
    print("Error while calling AI API:",error)
