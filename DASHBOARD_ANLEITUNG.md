# 🎓 CAS 2025 Dashboard - Bedienungsanleitung

## Übersicht

Das CAS 2025 Dashboard vereint alle Funktionen in einer zentralen Oberfläche:
- **Startseite**: Übersicht und Navigation
- **Herzfrequenz-Analyse**: Apple Health Pulsdaten-Analyse
- **Dokumenten-Portal**: CAS-Dokumenten-Download

## 🚀 Start des Dashboards

```bash
# Dashboard starten
streamlit run dashboard.py
```

Das Dashboard öffnet sich automatisch im Browser unter `http://localhost:8501`

## 📱 Navigation

### Sidebar (linke Seite)

Die Navigation erfolgt über die **Seitenleiste**:

1. **🏠 Startseite** - Hauptübersicht
2. **❤️ Herzfrequenz-Analyse** - Gesundheitsdaten-Analyse
3. **📚 Dokumenten-Download** - CAS-Dokumente herunterladen

**Zusätzliche Informationen in der Sidebar:**
- Aktuelle Seite
- Datum und Uhrzeit
- Bei Herzfrequenz-Analyse: Filter-Einstellungen

### Hauptbereich (Mitte)

Der Hauptbereich zeigt den Inhalt der ausgewählten Seite.

## 🏠 Startseite

### Funktionskarten

Zwei große Karten bieten direkten Zugriff:

**❤️ Herzfrequenz-Analyse**
- Zeitverlauf-Visualisierung
- Tagesstatistiken
- Tageszeit-Analyse
- Anomalie-Erkennung
- CSV-Export

**📚 Dokumenten-Download**
- Non-Binary Teacher Dokumentation
- CAS Programm 2025
- Transidentität Präsentation

### Übersichts-Statistiken

Drei Metrikkarten zeigen:
1. **Verfügbare Dokumente**: Anzahl der CAS-Dokumente (3)
2. **Herzfrequenz-Messungen**: Anzahl geladener Datenpunkte (oder "Keine Daten")
3. **Funktionen**: Anzahl der Hauptfunktionen (2)

### Schnellzugriff

Drei Info-Boxen mit Links und Status:
- **📖 Dokumentation**: Links zu README, Anleitung, Beispielen
- **✅ Status**: System-, Parser- und Dokumenten-Status
- **💡 Hinweis**: Wichtige Hinweise zu Datenschutz und Verarbeitung

## ❤️ Herzfrequenz-Analyse

### 1. Daten hochladen

**Upload-Bereich:**
- Button **"Browse files"** oder Drag & Drop
- Nur ZIP-Dateien werden akzeptiert
- Maximale Größe: 500 MB

**Verarbeitung:**
- Fortschrittsanzeige während des Uploads
- Automatische Extraktion der export.xml
- Parser lädt und analysiert Herzfrequenzdaten
- Bei Erfolg: Konfetti-Animation ✨

### 2. Übersichts-Statistiken

Nach erfolgreichem Upload werden vier Metriken angezeigt:

| Metrik | Beschreibung |
|--------|--------------|
| **Gesamtmessungen** | Anzahl aller Herzfrequenz-Datenpunkte |
| **Ø Herzfrequenz** | Durchschnittlicher Puls über alle Messungen |
| **Min / Max** | Niedrigster und höchster gemessener Wert |
| **Zeitraum** | Zeitspanne der Messungen in Tagen |

### 3. Filter-Optionen (Sidebar)

**Datumsfilter:**
1. Checkbox **"Datumsbereich einschränken"** aktivieren
2. Start- und Enddatum auswählen
3. Alle Visualisierungen werden automatisch aktualisiert

**Verwendung:**
- Fokus auf bestimmte Zeiträume (z.B. letzte 30 Tage)
- Vergleich verschiedener Perioden
- Ausschluss von Ausreißer-Zeiträumen

### 4. Visualisierungs-Tabs

#### Tab 1: 📈 Zeitverlauf

**Hauptdiagramm:**
- Liniendiagramm aller Herzfrequenzmessungen
- X-Achse: Zeitpunkt (Datum & Uhrzeit)
- Y-Achse: Herzfrequenz (bpm)
- Interaktiv: Zoom durch Anklicken und Ziehen
- Hover: Details zu jedem Datenpunkt

**Performance:**
- Bei großen Datenmengen (>1000 Punkte): Automatische Stichprobe
- Zeigt maximal 1000 Datenpunkte für bessere Performance
- Stichprobe ist repräsentativ für Gesamtdaten

#### Tab 2: 📊 Tagesstatistiken

**Tagesdiagramm:**
- Durchschnittliche Herzfrequenz pro Tag
- Liniendiagramm mit Markern
- Zeigt Trends über mehrere Tage/Wochen

**Interpretation:**
- Gleichmäßiger Verlauf → Stabiler Gesundheitszustand
- Anstieg → Stress, Krankheit, intensive Trainingsphase
- Abfall → Verbesserter Fitness-Level, Erholungsphase

#### Tab 3: 📋 Rohdaten

**Datentabelle:**
- Zeigt erste 100 Zeilen der gefilterten Daten
- Spalten: Timestamp, Herzfrequenz, Einheit, Quelle
- Scrollbar für Navigation

**CSV-Export:**
- Button **"📥 Daten als CSV exportieren"**
- Dateiname enthält aktuelles Datum
- Alle gefilterten Daten werden exportiert (nicht nur erste 100)

### 5. Workflow-Beispiel

**Szenario: Analyse der letzten 7 Tage**

1. ZIP-Datei hochladen
2. Warten bis Daten geladen sind
3. In Sidebar: "Datumsbereich einschränken" aktivieren
4. Letzte 7 Tage auswählen
5. Tab "Zeitverlauf" → Tagesverlauf betrachten
6. Tab "Tagesstatistiken" → Trendentwicklung prüfen
7. Tab "Rohdaten" → Bei Bedarf CSV exportieren

## 📚 Dokumenten-Portal

### Dokumentenliste

Drei Karten zeigen verfügbare Dokumente:

#### 1. Non-Binary Teacher Dokumentation
- **Format**: PDF
- **Größe**: ~61 KB
- **Beschreibung**: Dokumentation zum Thema Non-Binary Teacher

#### 2. CAS Programm 2025
- **Format**: DOCX
- **Größe**: ~31 KB  
- **Beschreibung**: Vollständiges Programm für den CAS 2025 Kurs

#### 3. Transidentität Teil 1 - CAS Präsentation
- **Format**: PPTX
- **Größe**: ~23 MB
- **Beschreibung**: Präsentation zum Thema Transidentität (Teil 1)

### Download-Prozess

1. Gewünschtes Dokument in der Liste finden
2. Auf Button **"📥 Download [FORMAT]"** klicken
3. Datei wird automatisch heruntergeladen
4. Im Download-Ordner des Browsers zu finden

### Dokumenten-Karten

**Hover-Effekt:**
- Bei Mausüberfahrt: Leichtes Verschieben nach rechts
- Schatten wird stärker
- Visuelles Feedback für Interaktivität

## 💡 Tipps zur Nutzung

### Dashboard-Performance

**Bei langsamer Performance:**
1. Nur eine Funktion gleichzeitig nutzen
2. Bei Herzfrequenz: Datumsfilter verwenden
3. Browser-Cache leeren
4. Andere Browser-Tabs schließen

### Navigation

**Schnelle Navigation:**
- Sidebar bleibt immer sichtbar
- Ein Klick wechselt die Seite
- Aktueller Standort wird in Sidebar angezeigt
- Zurück zur Startseite: 🏠 Button

### Daten-Workflow

**Empfohlener Ablauf:**
1. **Startseite**: Übersicht verschaffen
2. **Herzfrequenz-Analyse**: Daten hochladen und analysieren
3. **Dokumenten-Portal**: Relevante Dokumente herunterladen
4. Zurück zu **Startseite**: Nächste Aufgabe wählen

## 🎨 Design-Elemente

### Farbschema

- **Primärfarben**: Lila-Blau Gradient (#667eea → #764ba2)
- **Herzfrequenz**: Rot (#FF6B6B)
- **Info-Boxen**: Blau (#2196F3)
- **Erfolg**: Grün (#4caf50)
- **Warnung**: Orange (#ff9800)

### Karten-Typen

**Navigations-Karten (Startseite):**
- Großer Gradient-Hintergrund
- Hover-Effekt: Hebt sich an
- Call-to-Action Button

**Metrikkarten:**
- Weißer Hintergrund
- Dezenter Schatten
- Große Zahlen für Lesbarkeit

**Info-Boxen:**
- Farbig codiert nach Typ
- Linker farbiger Rand
- Kompakte Information

**Dokumenten-Karten:**
- Heller Hintergrund
- Linker Akzentbalken
- Hover-Effekt: Verschiebt sich

## 🔧 Fehlerbehebung

### "Seite lädt nicht"

**Lösungen:**
1. Browser neu laden (F5)
2. Cache leeren (Strg+Shift+R / Cmd+Shift+R)
3. Dashboard neu starten
4. Anderen Browser versuchen

### "Navigation funktioniert nicht"

**Lösungen:**
1. JavaScript im Browser aktiviert?
2. Seite vollständig geladen?
3. Dashboard neu starten
4. Browser-Konsole auf Fehler prüfen

### "Daten werden nicht angezeigt"

**Herzfrequenz-Analyse:**
1. ZIP-Datei korrekt hochgeladen?
2. Enthält die Datei export.xml?
3. Sind Herzfrequenzdaten in Health vorhanden?
4. Versuchen Sie erneuten Upload

**Dokumenten-Portal:**
1. Sind die Dokumente im Verzeichnis vorhanden?
2. Pfade korrekt?
3. Dateiberechtigungen prüfen

## 🔒 Datenschutz im Dashboard

### Lokale Verarbeitung

- **Alle Daten bleiben lokal**: Keine Cloud-Übertragung
- **Session-basiert**: Daten werden nicht dauerhaft gespeichert
- **Temporäre Dateien**: Automatische Löschung nach Verarbeitung

### Session State

Das Dashboard verwendet Streamlit Session State:
- Speichert Daten nur während der Browser-Sitzung
- Schließen des Browsers → alle Daten weg
- Neuladen der Seite → Daten bleiben (in Session)

### Empfehlungen

**Für maximalen Datenschutz:**
1. Dashboard lokal auf eigenem Computer ausführen
2. Nicht in öffentlichen Netzwerken verwenden
3. Browser-Sitzung nach Nutzung schließen
4. Keine Screenshots von sensiblen Daten erstellen

## 📊 Erweiterte Funktionen

### Multi-Tab-Nutzung

Sie können mehrere Browser-Tabs öffnen:
- **Tab 1**: Herzfrequenz-Analyse
- **Tab 2**: Dokumenten-Portal
- **Achtung**: Session State ist Tab-spezifisch!

### Mobile Nutzung

Das Dashboard ist responsive:
- Funktioniert auf Smartphones/Tablets
- Sidebar wird zu ausklappbarem Menü
- Touch-Gesten für Zoom in Diagrammen

### Keyboard-Shortcuts

**Streamlit Standard-Shortcuts:**
- `R`: App neu laden
- `C`: Menü öffnen/schließen
- `Esc`: Dialog schließen

## 🆘 Support

Bei Problemen:
1. Diese Anleitung vollständig lesen
2. README.md und andere Dokumentationen konsultieren
3. Demo-Skript testen: `python3 test_parser_demo.py`
4. Fehler-Logs in der Konsole prüfen

## 🔄 Updates

**Dashboard aktualisieren:**
```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

**Änderungen werden übernommen nach:**
- Dashboard-Neustart
- Browser-Neuladung (F5)

---

**Version**: 1.0  
**Erstellt**: Juli 2026  
**CAS 2025 Projekt**
