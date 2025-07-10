import os
import gspread
from google.oauth2.service_account import Credentials

SHEET_ID = '1fiITctTirAwsZxmvpzy4Mkfhv64sANKApgK5GTU6gAQ'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
CREDENTIALS_PATH = 'credentials/service_account.json'

def connect_to_sheet():
    json_str = os.getenv("GAC_PLRS") 

    if not json_str:
        raise ValueError("🔐 Variable de entorno GAC_PLRS no está definida")

    os.makedirs("credentials", exist_ok=True)
    with open(CREDENTIALS_PATH, "w") as f:
        f.write(json_str)

    creds = Credentials.from_service_account_file(CREDENTIALS_PATH, scopes=SCOPES)
    client = gspread.authorize(creds)
    return client.open_by_key(SHEET_ID)
