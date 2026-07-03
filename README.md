# CAS 2025 - Gesundheitsdaten & Dokumente Portal

Ein zentrales Dashboard mit zwei Hauptfunktionen:
1. **Apple Health Herzfrequenz-Analyse** - Analyse von Pulsdaten
2. **Dokumenten-Download Portal** - Download von CAS-Dokumenten

## 🚀 Lokale Nutzung

```bash
# Abhängigkeiten installieren
pip install -r requirements.txt

# Dashboard starten (empfohlen)
streamlit run dashboard.py

# ODER: Einzelne Apps starten
streamlit run heart_rate_app.py   # Nur Herzfrequenz-Analyse
streamlit run app.py                # Nur Dokumenten-Portal
```

Die App ist dann verfügbar unter:
- **Lokal:** http://localhost:8501
- **Lokales Netzwerk:** http://[Ihre-IP]:8501

## 🌍 Weltweite Verfügbarkeit

### Option 1: Streamlit Community Cloud (Kostenlos)
1. Code auf GitHub hochladen
2. Bei [share.streamlit.io](https://share.streamlit.io) anmelden
3. Repository verknüpfen
4. App automatisch deployen

### Option 2: Heroku (Kostenlos möglich)
1. Heroku-Account erstellen
2. Heroku CLI installieren
3. App deployen

### Option 3: Railway/Render (Kostenlos möglich)
Moderne Alternativen zu Heroku

## 🎯 Dashboard-Funktionen

### Startseite
- Übersicht über alle verfügbaren Funktionen
- Schnellnavigation zu Herzfrequenz-Analyse und Dokumenten-Portal
- System-Status und Statistiken

### ❤️ Herzfrequenz-Analyse

Analysieren Sie Ihre Herzfrequenzdaten aus Apple Health:

- 📊 Zeitverlauf-Visualisierung
- 📈 Tagesstatistiken und Trends  
- ⏰ Tageszeit-Analyse
- 🔍 Anomalie-Erkennung
- 📥 CSV-Export

**Dokumentation:**
- [README_HERZFREQUENZ.md](README_HERZFREQUENZ.md) - Technische Dokumentation
- [ANLEITUNG.md](ANLEITUNG.md) - Ausführliche Bedienungsanleitung

### 📚 Dokumenten-Portal

Zentrale Verwaltung aller CAS-Dokumente mit Download-Funktion.

## 📁 Verfügbare Dokumente

- `cas_nonbinaryteacher.pdf` - Non-Binary Teacher Dokumentation
- `CAS_Programm 2025.docx` - CAS Programm 2025
- `Transidentität_Teil1_CAS_22112024v3.pptx` - Transidentität Präsentation

## 🔒 Sicherheitshinweise

- Dokumente sind öffentlich downloadbar
- **Gesundheitsdaten werden nur lokal verarbeitet** (nicht gespeichert)
- Für sensible Daten: Authentifizierung hinzufügen
- HTTPS für Produktionsumgebung empfohlen 