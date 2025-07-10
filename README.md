# Polaris OSINT Forge 🚨🌐  
**ENGLISH:** Modular and ethical OSINT analysis system for the Knowmad Institut  
**ESPAÑOL:** Sistema modular y ético de análisis OSINT para el Knowmad Institut  
**DEUTSCH:** Modulares und ethisches OSINT-Analysesystem für das Knowmad Institut

---

## 🧠 What does this system do?  
**EN:**  
Polaris OSINT Forge is a semi-automated intelligence system for structured monitoring, narrative mapping, and ethical alerts based on open-source data. It connects news, videos, and social media feeds with sentiment models, geolocation engines, and clustering logic.

**ES:**  
Polaris OSINT Forge es un sistema de inteligencia semi-automatizado para monitoreo estructurado, mapeo narrativo y alertas éticas basadas en datos de fuente abierta. Conecta noticias, videos y redes sociales con modelos de sentimiento, geolocalización y lógica de clústeres.

**DE:**  
Polaris OSINT Forge ist ein halbautomatisches Intelligence-System für strukturiertes Monitoring, Narrativ-Mapping und ethische Alarme auf Basis von Open-Source-Daten. Es verbindet Nachrichten, Videos und soziale Medien mit Sentimentmodellen, Geolokalisierung und Clustering-Logik.

---

## 📡 Features  
- 🌐 Connects to news, videos, and alert feeds (Google Alerts, YouTube, RSS)  
- 🌍 Geolocation of events and actors (Google Maps API, Wayback archival)  
- 💬 Sentiment analysis via HuggingFace Transformers  
- 🧠 Narrative clustering and actor detection (LLM-ready output)  
- 📊 Exports live insights to Google Sheets  
- 🛡️ Built with auditability, transparency and FAIR/OSINT principles  

---

## 📁 Main Modules / Módulos Principales / Hauptmodule

| Script               | EN (Function)                                | ES (Función)                                   | DE (Funktion)                                  |
|----------------------|----------------------------------------------|------------------------------------------------|------------------------------------------------|
| `connect_sheet.py`   | Connects to Google Sheets via Service Account | Conecta con Google Sheets vía cuenta de servicio | Verbindung zu Google Sheets über Service-Konto |
| `youtube_alerts.py`  | Searches videos by keyword via YouTube API   | Busca videos por palabra clave (YouTube API)   | Sucht Videos nach Schlüsselwörtern (YouTube API) |
| `cluster_analysis.py`| Groups entries by narrative (advanced phase) | Agrupa entradas por narrativa (fase avanzada)  | Gruppiert Einträge nach Narrativ (fortgeschrittene Phase) |
| `geo_enrichment.py`  | Adds location coordinates & metadata         | Agrega coordenadas y metadatos geográficos     | Fügt Koordinaten und Geo-Metadaten hinzu        |
| `wayback.py`         | Archives or retrieves snapshots              | Archiva o recupera snapshots                   | Archiviert oder ruft Snapshots ab                |

---

## 🧪 Requirements / Requisitos / Voraussetzungen

```bash
pip install -r requirements.txt
Python 3.9+

Google Cloud Project (nonprofit/free tier)

HuggingFace Transformers (free API access)

GitHub & GitHub Actions (for automation)

Google Sheets API / YouTube Data API v3

🔐 Security and Ethics
EN:
No sensitive data or credentials are included. This repo reflects only the public-facing automation layer. The internal OSINT methodology, ethical protocols, and decision checklists are privately maintained by the Knowmad Institut.

ES:
Este repositorio no incluye datos sensibles ni credenciales. Refleja únicamente la capa de automatización pública. La metodología OSINT interna, los protocolos éticos y las listas de verificación se mantienen de forma privada por el Knowmad Institut.

DE:
Dieses Repository enthält keine sensiblen Daten oder Zugangsdaten. Es zeigt nur die öffentliche Automatisierungsschicht. Die interne OSINT-Methodik, ethische Protokolle und Entscheidungschecklisten werden privat vom Knowmad Institut gepflegt.

📄 License / Licencia / Lizenz
AGPLv3 — You may use, modify, and share this software, provided you keep the same license and share improvements.
AGPLv3 — Puedes usar, modificar y compartir este software, siempre que mantengas la misma licencia y compartas mejoras.
AGPLv3 — Du darfst diese Software verwenden, ändern und weitergeben, solange du dieselbe Lizenz beibehältst und Verbesserungen teilst.

🔗 View LICENSE

🌐 Aligned Institutions / Instituciones / Institutionen
🧠 Knowmad Institut
🌱 C4 Recovery Foundation
🕊️ Rome Consensus 2.0


🧭 OSINT for Human Dignity
EN: Open source intelligence as a tool for human rights, cognitive liberty, and sustainable peace.
ES: Inteligencia de fuente abierta como herramienta para los derechos humanos, la libertad cognitiva y la paz sostenible.
DE: Open-Source-Intelligence als Werkzeug für Menschenrechte, kognitive Freiheit und nachhaltigen Frieden.

📬 Contacto / Contact / Kontakt
contact@knowmadinstitut.org
https://knowmadinstitut.org
📄 Open Science Knowmad Research Gateway: https://bit.ly/knowmad-research
