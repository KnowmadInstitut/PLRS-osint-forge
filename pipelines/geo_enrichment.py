# geo_enrichment.py
# Utiliza servicios gratuitos (OpenStreetMap) para convertir nombres de lugares
# (ciudades, regiones) en coordenadas geográficas para su mapeo y análisis.

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import time

def get_coordinates(location_names):
    """
    Obtiene las coordenadas (latitud, longitud) para una lista de nombres de lugares.
    """
    # Inicializar el geocodificador de Nominatim con un user_agent único para tu app
    geolocator = Nominatim(user_agent="osint_drug_policy_monitor_v2")

    # RateLimiter para no sobrecargar el servidor de OpenStreetMap (1 petición por segundo)
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1, error_wait_seconds=10.0)

    results = {}
    print(f"[INFO] Procesando {len(location_names)} ubicaciones...")

    for name in location_names:
        try:
            location = geocode(name, addressdetails=True, language='es')
            if location:
                results[name] = {
                    'address': location.address,
                    'latitude': location.latitude,
                    'longitude': location.longitude
                }
                print(f"  [OK] Ubicación encontrada para '{name}'")
            else:
                results[name] = None
                print(f"  [AVISO] No se pudo encontrar la ubicación para '{name}'.")
        except Exception as e:
            print(f"  [ERROR] Ocurrió un error al procesar '{name}': {e}")
            results[name] = None

    return results

if __name__ == '__main__':
    # Ejemplo de ubicaciones que podrían extraerse de las noticias
    LOCATIONS_FROM_NEWS = [
        "Sinaloa, Mexico",
        "Puerto de Amberes, Bélgica",
        "Kensington, Philadelphia",
        "La Comuna 13, Medellín",
        "El Callao, Perú",
        "Una ciudad inexistente 123" # Ejemplo para probar el fallo
    ]

    print("--- INICIANDO ENRIQUECIMIENTO GEOGRÁFICO CON OPENSTREETMAP ---")
    coordinates_data = get_coordinates(LOCATIONS_FROM_NEWS)

    print("\n--- Resultados de Geocodificación ---")
    for location, data in coordinates_data.items():
        if data:
            print(f"\nLugar: {location}")
            print(f"  -> Dirección completa: {data['address']}")
            print(f"  -> Coordenadas: (Lat: {data['latitude']}, Lon: {data['longitude']})")
        else:
            print(f"\nLugar: {location} -> No se encontraron coordenadas.")
