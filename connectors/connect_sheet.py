import gspread
from google.oauth2.service_account import Credentials
import os
import json

# Crea archivo temporal a partir de variable de entorno (GAC_PLRS)
SERVICE_ACCOUNT_JSON = os.getenv("GAC_PLRS")

if not SERVICE_ACCOUNT_JSON:
    raise EnvironmentError("❌ No se encontró la variable de entorno GAC_PLRS")

# Ruta temporal segura
CREDENTIALS_PATH = "credentials/service_account.json"

# Crear el archivo si no existe
os.makedirs("credentials", exist_ok=True)
with open(CREDENTIALS_PATH, "w") as f:
    f.write(SERVICE_ACCOUNT_JSON)

# ID del Google Sheet
SHEET_ID = '1fiITctTirAwsZxmvpzy4Mkfhv64sANKApgK5GTU6gAQ'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def connect_to_sheet():
    creds = Credentials.from_service_account_file(CREDENTIALS_PATH, scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SHEET_ID)
    return sheet
