import gspread
from google.oauth2.service_account import Credentials

# Configura tu ruta local a la clave del Service Account
SERVICE_ACCOUNT_FILE = 'credentials/service_account.json'

# Este es tu ID real del Google Sheet
SHEET_ID = '1fiITctTirAwsZxmvpzy4Mkfhv64sANKApgK5GTU6gAQ'

# Alcances necesarios para Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def connect_to_sheet():
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SHEET_ID)
    return sheet
