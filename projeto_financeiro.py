import os
import pandas as pd
import requests
import json
from dotenv import load_dotenv
load_dotenv()

arquivo = "ResumoFinanceiro.xlsx"
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

#Filtro pra apagar as linhas testes
df = df[df["message_id"] >= 7]
print(df)
#

df["date"] = pd.to_datetime(df["date"], unit="s")

def limpar_mensagem(txt:str):
    valor = float(txt.split(" ")[0].replace(",", "."))
    descricao = txt.split(" ", 1)[1].rsplit(" ", 1)[0]
    forma_pagamento = txt.split(" ")[-1].upper()
    return valor, descricao, forma_pagamento

df["valor"] = df["text"].apply(lambda x: limpar_mensagem(x)[0])
df["descricao"] = df["text"].apply(lambda x: limpar_mensagem(x)[1])
df["forma_pagamento"] = df["text"].apply(lambda x: limpar_mensagem(x)[2])

df = df.drop("text", axis=1)

df.to_excel(f"Projeto_Financeiro/{arquivo}", sheet_name="Base", index=False, )

df_atual = pd.read_excel(f"Projeto_Financeiro/{arquivo}")

print(df_atual)