import os
import pandas as pd
import requests
import json
from openpyxl import load_workbook
from dotenv import load_dotenv
load_dotenv()

arquivo = "ResumoFinanceiro.xlsx"
caminho_arquivo = f"Projeto_Financeiro/{arquivo}"
api_key = os.getenv("api_key")
url = f"https://api.telegram.org/bot{api_key}/getUpdates"

def conectar_api(url):
    response = requests.get(url)
    data = response.json()
    data_result = data["result"]
    return data_result

def ler_mensagensDF(data_result):
    dados = []
    for item in data_result:
        mensagem = item["message"]
        dados.append({
            "message_id": mensagem.get("message_id"),
            "text": mensagem.get("text"),
            "date": mensagem.get("date")
        })
    df = pd.DataFrame(dados)
    df = df[df["message_id"] >= 7]
    return df

def transformar_mensagens(df):
    df["date"] = pd.to_datetime(df["date"], unit="s", utc=True)
    df["date"] = df["date"].dt.tz_convert("America/Sao_Paulo")
    df["data"] = df["date"].dt.date
    df["horas"] = df["date"].dt.time
    def limpar_mensagem(txt:str):
        valor = float(txt.split(" ")[0].replace(",", "."))
        descricao = txt.split(" ", 1)[1].rsplit(" ", 1)[0]
        forma_pagamento = txt.split(" ")[-1].upper()
        return valor, descricao, forma_pagamento
    
    df["valor"] = df["text"].apply(lambda x: limpar_mensagem(x)[0])
    df["descricao"] = df["text"].apply(lambda x: limpar_mensagem(x)[1])
    df["forma_pagamento"] = df["text"].apply(lambda x: limpar_mensagem(x)[2])
    df = df.drop(["text", "date"], axis=1)
    return df

def ler_excel(caminho_arquivo):
    df_atual = pd.read_excel(caminho_arquivo, sheet_name="Base")
    return df_atual

def transformarDFs(df_antigo, df):
    df_excel = pd.concat([df_antigo, df])
    df_excel = df_excel.drop_duplicates(subset="message_id")
    return df_excel

def salvar_arquivo(df_excel, caminho_arquivo):
    with pd.ExcelWriter(
        caminho_arquivo,
        engine='openpyxl',
        mode="a",
        if_sheet_exists="replace"
    ) as writer:
        df_excel.to_excel(writer, sheet_name = "Base", index = False)

if __name__ == "__main__":
    data_result = conectar_api(url)
    df_mensagens = ler_mensagensDF(data_result)
    df_novo = transformar_mensagens(df_mensagens)
    df_antigo = ler_excel(caminho_arquivo)
    df_final = transformarDFs(df_antigo, df_novo)
    salvar_arquivo(df_final, caminho_arquivo)