import os
import pandas as pd
import requests
import json
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("api_key")

url = f"https://api.telegram.org/bot{api_key}/getUpdates/"

response = requests.get(url)

print(response.json())