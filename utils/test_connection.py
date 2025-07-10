from connectors.connect_sheet import connect_to_sheet

def main():
    try:
        sheet = connect_to_sheet()
        worksheet = sheet.worksheet("Refinado")  # Cambia el nombre si es necesario
        records = worksheet.get_all_records()
        print("Conexión exitosa. Mostrando primeras 5 filas:\n")
        for row in records[:5]:
            print(row)
    except Exception as e:
        print("Error al conectar con Google Sheets:")
        print(e)

if __name__ == "__main__":
    main()
