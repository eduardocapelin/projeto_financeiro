import os
import pandas as pd
import requests
import json
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("api_key")

url = f"https://api.telegram.org/bot{api_key}/getUpdates"

response = requests.get(url)

data = response.json()

dataResult = data["result"]

dados = []

for item in dataResult:
    mensagem = item["message"]
    dados.append({
        "message_id": mensagem.get("message_id"),
        "text": mensagem.get("text"),
        "date": mensagem.get("date")
    })

df = pd.DataFrame(dados)

print(df)