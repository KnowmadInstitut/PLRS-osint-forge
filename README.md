# Polaris OSINT Forge 🚨🌐

**ESPAÑOL: Sistema modular y ético de análisis OSINT para el Knowmad Institut.**  
**ENGLISH: Modular and ethical OSINT analysis system for the Knowmad Institut.**  
**DEUTSCH: Modulares und ethisches OSINT-Analysesystem für das Knowmad Institut.**

Este repositorio contiene los scripts principales del ecosistema Polaris OSINT Forge, una infraestructura automatizada de inteligencia de fuentes abiertas enfocada en derechos humanos, políticas de drogas, sostenibilidad y libertad cognitiva.  
This repository contains the core scripts of the Polaris OSINT Forge ecosystem, an automated open-source intelligence infrastructure focused on human rights, drug policy, sustainability, and cognitive freedom.  
Dieses Repository enthält die Hauptskripte des Polaris OSINT Forge-Ökosystems, einer automatisierten Open-Source-Intelligence-Infrastruktur mit Fokus auf Menschenrechte, Drogenpolitik, Nachhaltigkeit und kognitive Freiheit.

---

## 🧠 ¿Qué hace este sistema?  
## 🧠 What does this system do?  
## 🧠 Was macht dieses System?

- 📡 Recolecta datos de noticias, videos y redes vía feeds y APIs  
  Collects news, video, and social media data via feeds and APIs  
  Sammelt Nachrichten-, Video- und Social-Media-Daten über Feeds und APIs  

- 🌍 Geolocaliza eventos y narrativas  
  Geolocates events and narratives  
  Geolokalisiert Ereignisse und Narrative  

- 🤖 Aplica modelos de sentimiento y análisis semántico (LLMs, HuggingFace)  
  Applies sentiment models and semantic analysis (LLMs, HuggingFace)  
  Wendet Stimmungsmodelle und semantische Analysen an (LLMs, HuggingFace)  

- 📊 Clasifica por clústeres narrativos, riesgo y actores clave  
  Classifies by narrative clusters, risk, and key actors  
  Klassifiziert nach narrativen Clustern, Risiken und Schlüsselakteuren  

- 🔄 Escribe y actualiza hojas de Google Sheets en tiempo real  
  Writes and updates Google Sheets in real-time  
  Schreibt und aktualisiert Google Sheets in Echtzeit  

---

## 📁 Módulos principales  
## 📁 Main Modules  
## 📁 Hauptmodule

| Script               | Función (ES)                                   | Function (EN)                                  | Funktion (DE)                                 |
|----------------------|-----------------------------------------------|------------------------------------------------|-----------------------------------------------|
| `connect_sheet.py`   | Conecta a Google Sheets vía Service Account   | Connects to Google Sheets via Service Account  | Verbindet mit Google Sheets über Service-Konto |
| `youtube_alerts.py`  | Busca videos por palabra clave (YouTube API)  | Searches videos by keyword (YouTube API)       | Sucht Videos nach Schlüsselwörtern (YouTube API) |
| `cluster_analysis.py`| Agrupa entradas por narrativa (fase avanzada) | Groups entries by narrative (advanced phase)   | Gruppiert Einträge nach Narrativ (fortgeschritten) |

---

## 🧪 Requisitos  
## 🧪 Requirements  
## 🧪 Voraussetzungen

Instala las dependencias:  
Install dependencies:  
Installiere die Abhängigkeiten:

```bash
pip install -r requirements.txt
🔐 Seguridad y ética
🔐 Security and Ethics
🔐 Sicherheit und Ethik

Este repositorio no incluye datos sensibles ni credenciales.
This repository does not include sensitive data or credentials.
Dieses Repository enthält keine sensiblen Daten oder Zugangsdaten.

Las hojas reales y auditorías OSINT completas se mantienen privadas.
Real OSINT sheets and full audits are kept private.
Echte OSINT-Datenblätter und vollständige Audits bleiben privat.

La metodología interna del Knowmad Institut se aplica parcialmente aquí por razones de ética y protección de informantes.
Knowmad Institut’s internal methodology is partially applied here for ethical and whistleblower protection reasons.
Die interne Methodik des Knowmad Instituts wird hier aus ethischen Gründen und zum Schutz von Hinweisgebern nur teilweise angewendet.

📝 Licencia / License / Lizenz
AGPLv3 — Puedes usar, modificar y compartir este software, siempre que mantengas la misma licencia y compartas cualquier mejora.
AGPLv3 — You may use, modify, and share this software as long as you keep the same license and share any improvements.
AGPLv3 — Du darfst diese Software verwenden, ändern und weitergeben, solange du dieselbe Lizenz beibehältst und Verbesserungen teilst.

Ver / See / Siehe: LICENSE

🤝 Instituciones aliadas / Partner Institutions / Partnerinstitutionen
🧠 Knowmad Institut
🔄 Polaris OSINT System
🕊️ Rome Consensus 2.0
🌱 C4 Recovery Foundation

🧭 OSINT para derechos humanos
🧭 OSINT for Human Rights
🧭 OSINT für Menschenrechte

📬 Contacto / Contact / Kontakt
contact@knowmadinstitut.org
https://knowmadinstitut.org
📄 Open Science Knowmad Research Gateway: https://bit.ly/knowmad-research
