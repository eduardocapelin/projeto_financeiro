# 💸 Projeto de Controle Financeiro via Telegram

Este projeto foi desenvolvido para ajudar pessoas a manterem o controle de pequenos gastos do dia a dia. Muitas vezes fazemos compras pequenas que esquecemos de anotar, e no fim do mês isso pesa. Com esse código, basta enviar uma mensagem no Telegram com o valor, descrição e forma de pagamento, e os dados serão automaticamente registrados em um arquivo Excel para facilitar a análise financeira.

---

## 🎯 Objetivo

O principal objetivo é automatizar o registro de pequenas despesas, garantindo que nenhuma compra passe despercebida. O usuário só precisa enviar uma mensagem no formato correto para o bot no Telegram, e o sistema cuida do resto:

- Captura da mensagem via API do Telegram
- Transformação da mensagem em dados estruturados
- Armazenamento em uma planilha Excel
- Evita perda de informação e facilita a análise dos gastos

---

## 🛠 Tecnologias Utilizadas

- **Python** – linguagem principal
- **pandas** – manipulação de dados
- **requests** – requisições HTTP
- **dotenv** – gerenciamento de variáveis de ambiente
- **openpyxl** – escrita em planilhas Excel (.xlsx)
- **Telegram Bot API** – leitura das mensagens enviadas ao bot

---

## ⚙️ Como o Código Funciona

1. **Leitura de mensagens no Telegram:**
   - Utiliza o token do bot armazenado no `.env`
   - Faz uma requisição à API do Telegram para obter as mensagens recentes

2. **Transformação dos dados:**
   - Extrai `valor`, `descrição` e `forma_pagamento` da mensagem
   - Converte a data da mensagem para o formato datetime

3. **Leitura e atualização da planilha:**
   - Abre o arquivo Excel existente (mantendo outras abas intactas)
   - Adiciona os novos registros na aba "Base", evitando duplicações

4. **Gravação final:**
   - Salva a nova versão do arquivo Excel com os dados atualizados

---

## 📦 Estrutura Esperada da Mensagem no Telegram

Envie mensagens no seguinte formato para o bot:

49,90 Pizza PIX

- **Valor**: número com vírgula ou ponto  
- **Descrição**: parte central da mensagem  
- **Forma de pagamento**: última palavra (ex: PIX, Cartão, Dinheiro)

---

Com esse fluxo simples, você consegue manter seu controle financeiro atualizado com rapidez e sem complicações.