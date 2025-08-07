# cluster_analysis.py
# Aplica técnicas de clustering a datos de texto (noticias, reportes)
# para identificar narrativas y patrones emergentes de forma automática.

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def group_narratives(text_data, num_clusters=5):
    """
    Analiza una lista de textos (titulares, resúmenes) y los agrupa en clusters.
    Utiliza PCA para poder visualizar los clusters en 2D.
    """
    # Vectorizar el texto: convierte el texto en una matriz numérica.
    # Se ajustan los parámetros para capturar frases más relevantes.
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.9, min_df=2, ngram_range=(1,3))
    X = vectorizer.fit_transform(text_data)

    # Aplicar el algoritmo de clustering K-Means
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    kmeans.fit(X)

    # Reducir la dimensionalidad para visualización
    pca = PCA(n_components=2, random_state=42)
    reduced_features = pca.fit_transform(X.toarray())
    reduced_cluster_centers = pca.transform(kmeans.cluster_centers_)

    # Devolver las etiquetas, los datos reducidos y los centros para el gráfico
    return kmeans.labels_, reduced_features, reduced_cluster_centers

if __name__ == '__main__':
    # --- Conjunto de datos de ejemplo para el sistema OSINT ---
    # En un caso real, estos datos vendrían de tu monitoreo mediático (RSS, APIs, etc.).
    data = {
        'headline': [
            "Gobierno anuncia nueva estrategia de seguridad contra el narcotráfico",
            "Aumentan las muertes por sobredosis de fentanilo en la ciudad",
            "Nuevo centro de tratamiento ofrece ayuda para la adicción con naloxona",
            "La policía desmantela una red de distribución de drogas sintéticas",
            "Debate en el congreso sobre la legalización del cannabis recreativo",
            "Campaña de salud pública advierte sobre los peligros del fentanilo",
            "Jueces proponen alternativas a la cárcel para delitos de posesión de drogas",
            "Organizaciones piden expandir programas de reducción de daños y jeringuillas",
            "Reporte indica un aumento en el consumo de nuevas sustancias psicoactivas (NPS)",
            "El Cártel de Sinaloa refuerza sus fronteras para frenar el tráfico de drogas",
            "La crisis de opioides se agrava con la llegada de los nitazenos",
            "Discuten la regulación del mercado de cannabis medicinal en el senado",
            "Detienen a un capo del CJNG en un operativo federal",
            "Expertos en salud mental alertan sobre la adicción a las drogas de diseño",
        ]
    }
    df = pd.DataFrame(data)

    print("--- ANALIZANDO NARRATIVAS EN TITULARES MEDIÁTICOS ---")

    NUM_NARRATIVAS = 4
    clusters, reduced_data, centers = group_narratives(df['headline'], num_clusters=NUM_NARRATIVAS)
    df['narrative_group'] = clusters

    print("\nResultados del Análisis de Clusters:")
    # Imprimir los resultados agrupados
    for i in range(NUM_NARRATIVAS):
        print(f"\n--- Narrativa Grupo {i+1} ---")
        group_headlines = df[df['narrative_group'] == i]['headline'].tolist()
        for headline in group_headlines:
            print(f"  - {headline}")

    # Visualización de los clusters
    plt.figure(figsize=(10, 8))
    plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=clusters, cmap='viridis', marker='o')
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=250, marker='X', label='Centroides')
    plt.title('Visualización de Narrativas Mediáticas')
    plt.xlabel('Componente Principal 1')
    plt.ylabel('Componente Principal 2')
    plt.legend()
    plt.grid(True)
    plt.show()
