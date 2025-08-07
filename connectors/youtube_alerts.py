# youtube_alerts.py
# Realiza búsquedas periódicas en YouTube para monitorear contenido
# relacionado con políticas de drogas, seguridad y salud pública.
# VERSIÓN 3.0 - CONFIGURACIÓN OSINT EXHAUSTIVA Y PROFESIONAL

from googleapiclient.discovery import build
import time
import os

def Youtube(api_key, query, max_results=15):
    """
    Busca videos en YouTube basados en una consulta OSINT específica.
    """
    youtube = build('youtube', 'v3', developerKey=api_key)

    search_response = youtube.search().list(
        q=f'"{query}"',  # Búsqueda de frase exacta para mayor precisión
        part='id,snippet',
        type='video',
        order='date',
        maxResults=max_results
    ).execute()

    videos = []
    for search_result in search_response.get('items', []):
        video_info = {
            'title': search_result['snippet']['title'],
            'published_at': search_result['snippet']['publishedAt'],
            'channel': search_result['snippet']['channelTitle'],
            'url': f"https://www.youtube.com/watch?v={search_result['id']['videoId']}"
        }
        videos.append(video_info)
    return videos

if __name__ == '__main__':
    API_KEY = os.getenv('YOUTUBE_API_KEY', 'TU_API_KEY')

    # ==============================================================================
    # == CONFIGURACIÓN DE BÚSQUEDA OSINT DEFINITIVA
    # ==============================================================================
    OSINT_QUERIES = {
        # --- 1. Salud Pública, Tratamiento y Rehabilitación ---
        "Salud y Rehabilitación": [
            "salud y drogas", "drug rehabilitation", "rehabilitación de adicciones",
            "prevención de recaídas", "relapse prevention", "comunidad terapéutica",
            "crisis de opioides", "opioid crisis", "muertes por sobredosis", "overdose deaths",
            "naloxona", "naloxone", "reducción de daños", "harm reduction", "patología dual",
            "salud mental y adicción", "programas de intercambio de jeringuillas"
        ],

        # --- 2. Drogas Sintéticas, NPS y Precursores Químicos ---
        "Sintéticos y NPS": [
            "drogas sintéticas", "synthetic drugs", "nuevas sustancias psicoactivas", "NPS",
            "fentanilo", "fentanyl analogues", "opioides sintéticos", "synthetic opioids",
            "nitazenos", "nitazenes", "isotonitazene", "metonitazene",
            "cannabinoides sintéticos", "synthetic cannabinoids", "spice K2",
            "catinonas sintéticas", "synthetic cathinones", "sales de baño", "bath salts",
            "tusi", "cocaína rosa", "ketamina", "ketamine", "precursores químicos", "chemical precursors"
        ],

        # --- 3. Crimen Organizado y Tráfico Internacional ---
        "Crimen Organizado y Tráfico": [
            "narcotráfico", "drug trafficking", "incautación de drogas", "drug seizure",
            "Cártel de Sinaloa", "CJNG", "Ndrangheta", "Mocro Maffia",
            "ruta de la droga", "drug route", "tráfico en puertos", "port drug trafficking",
            "violencia por drogas", "drug related violence"
        ],

        # --- 4. Corrupción y Narcopolítica ---
        "Corrupción y Narcopolítica": [
            "corrupción y drogas", "narco-politics", "narcopolítica", "narcoestado", "narco state",
            "corrupción policial drogas", "police corruption drugs", "financiación ilícita",
            "lavado de dinero", "money laundering", "soborno narcotráfico"
        ],

        # --- 5. Ciberdelito y Mercados Darknet ---
        "Ciberdelito y Mercados": [
            "cibercrimen y drogas", "darknet markets", "mercados darknet",
            "venta de drogas telegram", "drug selling telegram", "venta drogas bitcoin",
            "silk road", "alphabay", "drug vendors online"
        ],

        # --- 6. Política, Justicia y Marco Regulatorio ---
        "Política y Justicia": [
            "política de drogas", "drug policy", "legalización", "legalization",
            "despenalización", "decriminalization", "regulación cannabis",
            "guerra contra las drogas", "war on drugs"
        ]
    }

    print("--- INICIANDO SISTEMA DE ALERTA TEMPRANA (CONFIGURACIÓN DEFINITIVA) ---")

    while True:
        for category, queries in OSINT_QUERIES.items():
            print(f"\n[INFO] Monitoreando categoría: '{category}'")
            for query in queries:
                print(f"  -> Buscando: \"{query}\"")
                try:
                    latest_videos = Youtube(API_KEY, query)
                    if not latest_videos:
                        continue

                    print(f"    -> [ALERTA] Se encontraron {len(latest_videos)} resultados para \"{query}\"")
                    for video in latest_videos:
                        print(f"        - {video['published_at'][:10]} | {video['title']} | {video['channel']}")
                        print(f"          URL: {video['url']}")

                except Exception as e:
                    print(f"    [ERROR] Ocurrió un error al buscar \"{query}\": {e}")

                time.sleep(5)

        print("\n--- CICLO COMPLETO. ESPERANDO 1 HORA PARA EL SIGUIENTE MONITOREO. ---")
        time.sleep(3600)
