import os
import json
import gspread
from google.oauth2.service_account import Credentials

SHEET_ID = '1fiITctTirAwsZxmvpzy4Mkfhv64sANKApgK5GTU6gAQ'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def connect_to_sheet():
    json_str = os.getenv("GAC_PLRS") 
    if not json_str:
        raise ValueError("🔐 Variable de entorno GAC_PLRS no está definida")

    service_account_info = json.loads(json_str)
    creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
    client = gspread.authorize(creds)
    return client.open_by_key(SHEET_ID)
