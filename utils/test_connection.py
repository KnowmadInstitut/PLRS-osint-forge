from connectors.connect_sheet import connect_to_sheet

def main():
    try:
        sheet = connect_to_sheet()
        worksheet = sheet.worksheet("Refinado")  # Asegúrate que esta hoja exista
        records = worksheet.get_all_records()
        print("✅ Conexión exitosa. Mostrando primeras 5 filas:\n")
        for row in records[:5]:
            print(row)
    except Exception as e:
        import traceback
        print("❌ Error al conectar con Google Sheets:")
        traceback.print_exc()  # 🧠 Esto mostrará exactamente qué falló

if __name__ == "__main__":
    main()
