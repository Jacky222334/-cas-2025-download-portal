# ❤️ Apple Health Herzfrequenz Analyse

Eine Streamlit-Anwendung zur Analyse und Visualisierung von Herzfrequenzdaten aus Apple Health.

## 🎯 Funktionen

- **Datenimport**: Upload von Apple Health Export ZIP-Dateien
- **Zeitverlauf-Visualisierung**: Grafische Darstellung der Herzfrequenz über die Zeit
- **Tagesstatistiken**: Durchschnittliche, minimale und maximale Werte pro Tag
- **Tageszeit-Analyse**: Erkennung von Mustern nach Uhrzeit
- **Anomalie-Erkennung**: Identifikation ungewöhnlicher Herzfrequenzwerte
- **Datenfilterung**: Eingrenzung nach Datumsbereich
- **CSV-Export**: Download der analysierten Daten

## 🚀 Installation und Nutzung

### Lokale Nutzung

```bash
# Abhängigkeiten installieren
pip install -r requirements.txt

# App starten
streamlit run heart_rate_app.py
```

Die App ist dann verfügbar unter: **http://localhost:8501**

### Alternative: Dokument-Download-Portal

```bash
streamlit run app.py
```

## 📱 Apple Health Daten exportieren

So exportieren Sie Ihre Herzfrequenzdaten aus Apple Health:

1. Öffnen Sie die **Health-App** auf Ihrem iPhone
2. Tippen Sie auf Ihr **Profilbild** oben rechts
3. Scrollen Sie nach unten zu **„Alle Gesundheitsdaten exportieren"**
4. Warten Sie, bis die ZIP-Datei erstellt wurde
5. Teilen/Exportieren Sie die Datei (z.B. per AirDrop, E-Mail oder Cloud)
6. Laden Sie die ZIP-Datei in der Web-App hoch

**Hinweis**: Der Export kann mehrere Minuten dauern, besonders bei vielen Daten.

## 📊 Funktionsübersicht

### Hauptstatistiken

- **Gesamtanzahl der Messungen**: Wie oft wurde Ihre Herzfrequenz erfasst
- **Durchschnittliche Herzfrequenz**: Mittlerer Puls über alle Messungen
- **Minimum/Maximum**: Niedrigster und höchster gemessener Wert
- **Zeitraum**: Dauer der erfassten Messungen in Tagen

### Visualisierungen

1. **Zeitverlauf**
   - Liniendiagramm aller Herzfrequenzmessungen
   - Verteilungshistogramm
   - Optional: Darstellung erkannter Anomalien

2. **Tagesstatistiken**
   - Tägliche Durchschnittswerte mit Min/Max-Bereichen
   - Tabellarische Übersicht aller Tageswerte
   - Erkennung von Trends

3. **Tageszeit-Analyse**
   - Durchschnittliche Herzfrequenz nach Stunde
   - Balkendiagramm zur Mustererkennung
   - Interpretation typischer Tagesverläufe

### Anomalie-Erkennung

Die App kann ungewöhnliche Herzfrequenzwerte identifizieren:

- **Algorithmus**: Statistische Ausreißererkennung basierend auf Standardabweichungen
- **Einstellbar**: Empfindlichkeit anpassbar (1,5 bis 4,0 Standardabweichungen)
- **Ausgabe**: Liste aller erkannten Anomalien mit Zeitstempel und Quelle

## 🔧 Technische Details

### Komponenten

- **`apple_health_parser.py`**: Parser für Apple Health XML-Dateien
  - Extraktion von Herzfrequenzdaten
  - Statistische Analysen
  - Datenfilterung und -aggregation
  - Anomalie-Erkennung

- **`heart_rate_app.py`**: Streamlit Web-Anwendung
  - Datei-Upload und -Verarbeitung
  - Interaktive Visualisierungen mit Plotly
  - Datenfilterung und -export
  - Benutzerfreundliche Oberfläche

### Datenstruktur

Apple Health exportiert Daten als XML-Datei mit folgender Struktur:

```xml
<Record type="HKQuantityTypeIdentifierHeartRate"
        startDate="2024-11-22 10:30:00 +0000"
        value="72"
        unit="count/min"
        sourceName="Apple Watch" />
```

### Extrahierte Informationen

- **Zeitstempel**: Wann wurde die Messung durchgeführt
- **Herzfrequenz**: Pulsschläge pro Minute (bpm)
- **Einheit**: Üblicherweise "count/min"
- **Quelle**: Gerät/App, die die Messung erfasst hat (z.B. Apple Watch, iPhone)

## 📈 Interpretationshilfen

### Normale Herzfrequenzbereiche

- **Ruhepuls (Erwachsene)**: 60-100 bpm
- **Sportler**: 40-60 bpm möglich
- **Während Aktivität**: 100-170+ bpm (altersabhängig)
- **Nachts/Schlaf**: Oft niedriger als Tagesdurchschnitt

### Tageszeit-Muster

- **Frühmorgens (4-7 Uhr)**: Niedrigste Werte (Ruhephase)
- **Vormittag (9-12 Uhr)**: Anstieg durch Aktivität
- **Nachmittag (14-18 Uhr)**: Oft höchste Durchschnittswerte
- **Abends (20-23 Uhr)**: Allmähliches Absinken

### Hinweise zu Anomalien

**Mögliche Ursachen für hohe Werte:**
- Körperliche Aktivität/Sport
- Stress oder Aufregung
- Koffein oder Medikamente
- Krankheit/Fieber

**Mögliche Ursachen für niedrige Werte:**
- Tiefer Schlaf
- Sehr gute Fitness
- Bestimmte Medikamente
- Entspannung/Meditation

**⚠️ Wichtig**: Diese App dient nur zu Informationszwecken. Bei gesundheitlichen Bedenken konsultieren Sie bitte einen Arzt.

## 🔒 Datenschutz

- **Lokale Verarbeitung**: Alle Daten werden nur lokal in Ihrem Browser/auf dem Server verarbeitet
- **Keine Speicherung**: Daten werden nicht dauerhaft gespeichert
- **Keine Weitergabe**: Keine Übertragung an Dritte
- **Temporäre Dateien**: Hochgeladene Dateien werden nach Verarbeitung gelöscht

## 🛠️ Entwicklung

### Projektstruktur

```
/workspace/
├── heart_rate_app.py           # Hauptanwendung
├── apple_health_parser.py      # Datenparser
├── app.py                      # Original Dokument-Portal
├── requirements.txt            # Python-Abhängigkeiten
├── README_HERZFREQUENZ.md      # Diese Dokumentation
└── README.md                   # Original-Dokumentation
```

### Erweiterungsmöglichkeiten

- **Weitere Metriken**: Schlaf, Schritte, Training
- **Vergleichsanalysen**: Korrelation verschiedener Gesundheitsdaten
- **Export-Formate**: PDF-Reports, Excel-Dateien
- **Langzeit-Trends**: Monats- und Jahresübersichten
- **Herzfrequenzvariabilität (HRV)**: Erweiterte Analysen

## 📦 Abhängigkeiten

- **streamlit**: Web-Framework
- **pandas**: Datenmanipulation und -analyse
- **plotly**: Interaktive Visualisierungen
- **xml.etree.ElementTree**: XML-Parsing (Standard-Bibliothek)

## 🤝 Beitragen

Verbesserungsvorschläge und Erweiterungen sind willkommen!

## 📄 Lizenz

Für Bildungszwecke entwickelt (CAS 2025).
