import os
import json
import gspread
from google.oauth2.service_account import Credentials

# Recupera las credenciales desde una variable de entorno (inyectada por GitHub Secrets)
credentials_json = os.getenv("GAC_PLRS")

if not credentials_json:
    raise EnvironmentError("La variable de entorno 'GAC_PLRS' no está definida.")

# Convierte el string JSON a un diccionario
info = json.loads(credentials_json)

# Alcances necesarios para Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Crea las credenciales desde el diccionario
creds = Credentials.from_service_account_info(info, scopes=SCOPES)

# ID del Google Sheet compartido
SHEET_ID = '1fiITctTirAwsZxmvpzy4Mkfhv64sANKApgK5GTU6gAQ'

def connect_to_sheet():
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SHEET_ID)
    return sheet
