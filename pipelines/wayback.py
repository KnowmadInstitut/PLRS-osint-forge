# wayback.py
# Archiva URLs de fuentes abiertas (noticias, blogs, reportes) en la Wayback Machine
# para preservar la evidencia digital y protegerla contra cambios o eliminaciones.

import waybackpy
import os

def archive_source(url, user_agent=None):
    """
    Guarda una instantánea de una URL en el Internet Archive's Wayback Machine.
    """
    if user_agent is None:
        # Es una buena práctica usar un user_agent que identifique a tu bot/proyecto.
        user_agent = os.getenv('OSINT_USER_AGENT', "OSINT Drug Policy Monitor Bot v2.0")

    try:
        print(f"[INFO] Intentando archivar la URL: {url}")
        archive = waybackpy.Url(url, user_agent).save()
        print(f"  [ÉXITO] La URL ha sido archivada correctamente.")
        return archive.archive_url
    except waybackpy.exceptions.BlockedByRobotsError:
        print(f"  [AVISO] El archivado de '{url}' está bloqueado por el archivo robots.txt del sitio.")
        return None
    except Exception as e:
        print(f"  [ERROR] No se pudo archivar la URL. Razón: {e}")
        return None

if __name__ == '__main__':
    # Ejemplo: URLs que podrían venir de tu sistema de alertas.
    URLS_TO_PRESERVE = [
        "https://www.unodc.org/unodc/en/data-and-analysis/world-drug-report-2023.html",
        "https://www.emcdda.europa.eu/publications/european-drug-report/2023_en",
        "http://pagina-que-no-existe-12345.com" # Ejemplo de URL que fallará
    ]

    print("--- INICIANDO MÓDULO DE ARCHIVO DE FUENTES DIGITALES ---")

    for url in URLS_TO_PRESERVE:
        archived_link = archive_source(url)

        if archived_link:
            print(f"  -> Enlace permanente: {archived_link}\n")
        else:
            print(f"  -> El proceso de archivo para esta URL falló.\n")
