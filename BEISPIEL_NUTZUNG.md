# 🚀 Beispiel: Apple Health Herzfrequenz-Analyse

## Schnelltest der Anwendung

### 1. Installation und Start

```bash
# Repository klonen (falls noch nicht geschehen)
cd /workspace

# Dependencies installieren
pip install -r requirements.txt

# App starten
streamlit run heart_rate_app.py
```

Die Anwendung öffnet sich unter: `http://localhost:8501`

### 2. Apple Health Daten vorbereiten

#### Auf dem iPhone:

1. **Health-App** öffnen
2. **Profilbild** oben rechts antippen
3. Nach unten scrollen
4. **"Alle Gesundheitsdaten exportieren"** wählen
5. Warten (kann 2-10 Minuten dauern je nach Datenmenge)
6. ZIP-Datei per AirDrop auf Mac übertragen oder per E-Mail/Cloud teilen

**Dateigröße**: Je nach Nutzungsdauer 10 MB - 500 MB

#### Datenstruktur der Export-Datei

Die ZIP-Datei enthält:
```
export.zip
└── apple_health_export/
    ├── export.xml          ← Hauptdatei mit allen Gesundheitsdaten
    ├── export_cda.xml      
    └── workout-routes/
```

Die App benötigt nur die `export.xml` Datei.

### 3. Daten in der App hochladen

1. Auf **"Browse files"** klicken
2. Die `.zip` Datei auswählen
3. Warten während die Verarbeitung läuft (5-30 Sekunden je nach Größe)
4. Bei Erfolg: Konfetti-Animation und Übersichts-Statistiken erscheinen

### 4. Beispiel-Analysen

#### Szenario A: Überblick über letzte 30 Tage

1. In der **Seitenleiste**:
   - ☑️ "Datumsbereich einschränken" aktivieren
   - Letzte 30 Tage auswählen
2. **Tab "Zeitverlauf"** öffnen
3. Beobachtung: Gesamttrend über den Monat

**Was zu erwarten ist:**
- Durchschnittlicher Ruhepuls: 60-80 bpm (Erwachsene)
- Spitzen während Aktivität: 100-170+ bpm
- Nachts niedrigere Werte: 50-70 bpm

#### Szenario B: Tagesrhythmus erkennen

1. **Tab "Tageszeit-Analyse"** öffnen
2. Balkendiagramm betrachten

**Typisches Muster:**
- **4-7 Uhr**: Niedrigste Werte (ca. 55-65 bpm) - Tiefschlafphase
- **7-9 Uhr**: Anstieg (ca. 70-80 bpm) - Aufwachen
- **12-14 Uhr**: Mittelwerte (ca. 75-85 bpm) - Mittagszeit
- **15-18 Uhr**: Höchste Werte (ca. 80-95 bpm) - Nachmittagsaktivität
- **22-24 Uhr**: Abnahme (ca. 70-75 bpm) - Entspannung vor dem Schlaf

**Abweichungen können bedeuten:**
- Sport zu bestimmten Zeiten
- Koffeinkonsum
- Stressige Arbeitszeiten
- Unregelmäßiger Schlafrhythmus

#### Szenario C: Ungewöhnliche Werte finden

1. **Seitenleiste** öffnen
2. ☑️ "Anomalien anzeigen" aktivieren
3. Empfindlichkeit auf **2,5** setzen (etwas sensitiver)
4. **Tab "Zeitverlauf"** → Nach unten scrollen zur Anomalien-Tabelle

**Interpretation der Anomalien:**

| Herzfrequenz | Mögliche Ursache | Bewertung |
|--------------|------------------|-----------|
| > 150 bpm | Intensive körperliche Aktivität, Sport | Normal |
| > 180 bpm | Sehr intensive Aktivität oder Stress | Beachten |
| < 45 bpm (nachts) | Tiefer Schlaf, gute Fitness | Normal bei Sportlern |
| < 40 bpm (tagsüber) | Sehr gute Fitness oder Messfehler | Prüfen |

#### Szenario D: Wöchlicher Vergleich

1. **Tab "Tagesstatistiken"** öffnen
2. Liniendiagramm mit täglichen Durchschnittswerten betrachten
3. Tabellarische Ansicht für genaue Zahlen nutzen

**Mögliche Erkenntnisse:**
- **Gleichmäßiger Verlauf**: Stabiler Gesundheitszustand
- **Anstieg über mehrere Tage**: Stress, Krankheit, intensive Trainingswoche
- **Abfall über mehrere Tage**: Verbesserter Fitness-Level, Erholungsphase
- **Große Schwankungen**: Unregelmäßiger Lebensstil, wechselnde Aktivitätslevel

### 5. Daten exportieren

#### CSV-Export für eigene Analysen

1. **Tab "Rohdaten"** öffnen
2. Button **"📥 Daten als CSV exportieren"** klicken
3. Datei wird heruntergeladen (z.B. `herzfrequenz_daten_20260702.csv`)

**CSV-Struktur:**
```csv
timestamp,heart_rate,unit,source
2024-11-22 08:30:15,72,count/min,Apple Watch
2024-11-22 08:35:20,75,count/min,Apple Watch
2024-11-22 09:12:45,68,count/min,Apple Watch
```

**Verwendung der CSV:**
- Excel/Numbers: Pivot-Tabellen, eigene Diagramme
- R/Python: Statistische Analysen, Machine Learning
- Teilen mit Arzt/Trainer
- Langzeit-Archivierung

### 6. Beispiel-Befunde

#### Fall 1: Verbesserung der Fitness

**Beobachtung über 3 Monate:**
- Monat 1: Ø Ruhepuls 78 bpm
- Monat 2: Ø Ruhepuls 74 bpm  
- Monat 3: Ø Ruhepuls 68 bpm

**Interpretation**: 
→ Herzkreislauf-System hat sich durch Training verbessert
→ Niedrigerer Ruhepuls = effizienter arbeitendes Herz

#### Fall 2: Stress-Erkennung

**Beobachtung:**
- Normale Woche: Ø Tagespuls 72 bpm
- Projekt-Deadline-Woche: Ø Tagespuls 85 bpm
- Nachts: Puls bleibt erhöht (65-70 statt 55-60 bpm)

**Interpretation**:
→ Erhöhter Stress-Level erkennbar
→ Reduzierte Erholungsqualität im Schlaf
→ Möglicherweise Bedarf für Entspannungsmaßnahmen

#### Fall 3: Koffein-Wirkung

**Beobachtung im Tagesverlauf:**
- 6:00 Uhr: 58 bpm (Aufwachen)
- 7:00 Uhr: 72 bpm (nach Kaffee)
- 8:00 Uhr: 78 bpm (1h nach Kaffee)
- 11:00 Uhr: 68 bpm (Koffein-Wirkung lässt nach)

**Interpretation**:
→ Deutlicher Koffein-Effekt sichtbar
→ Peak 1h nach Konsum
→ Wirkung hält ca. 3-4 Stunden

## 💡 Tipps für aussagekräftige Analysen

### Datenqualität verbessern

**Apple Watch Träger:**
- Uhr eng am Handgelenk tragen
- Regelmäßige Messung aktiviert lassen
- Während Sport: Workout-Modus nutzen

**iPhone-Only Nutzer:**
- Health-App mit anderen Apps verknüpfen (z.B. Fitness-Apps)
- Manuelle Messungen regelmäßig durchführen
- Externe Geräte anbinden (Fitness-Tracker, Brustgurt)

### Analysezeiträume

**Kurze Analysen (1-7 Tage):**
- Akute Veränderungen erkennen
- Tagesrhythmus verstehen
- Aktivitäts-Impact messen

**Mittlere Analysen (1-3 Monate):**
- Trainings-Fortschritte verfolgen
- Lifestyle-Änderungen bewerten
- Saisonale Muster erkennen

**Lange Analysen (6-12+ Monate):**
- Fitness-Entwicklung dokumentieren
- Gesundheits-Trends erkennen
- Medizinische Verlaufskontrolle

### Performance-Optimierung

Bei sehr großen Datenmengen (>50.000 Messungen):

1. **Datumsfilter nutzen**: Monat für Monat analysieren
2. **Datenpunkt-Limit reduzieren**: Slider auf 500-1000 setzen
3. **Browser-Cache leeren**: Bei langsamer Performance
4. **Lokale Installation**: Schneller als Cloud-Deployment

## 🩺 Praktische Anwendungsfälle

### Für Sportler

- Training-Load-Management
- Übertraining-Erkennung (erhöhter Ruhepuls)
- Erholungs-Monitoring
- Wettkampf-Vorbereitung

### Für Gesundheitsbewusste

- Stress-Level-Tracking
- Lifestyle-Änderungen quantifizieren
- Schlafqualität indirekt bewerten
- Langzeit-Gesundheitstrends

### Für Patienten (in Absprache mit Arzt)

- Medikamenten-Wirkung dokumentieren
- Post-OP-Verlauf monitoren
- Chronische Erkrankungen tracken
- Arztbesuche vorbereiten (Daten mitbringen)

## ⚠️ Wichtige Einschränkungen

**Diese App ist KEIN Ersatz für:**
- Medizinische Diagnostik
- Professionelle Gesundheitsberatung
- Notfall-Monitoring
- Behandlungsempfehlungen

**Wann Sie einen Arzt konsultieren sollten:**
- Unregelmäßiger Herzschlag
- Herzrasen ohne erkennbaren Grund
- Sehr niedriger Puls mit Symptomen
- Plötzliche drastische Veränderungen
- Begleitsymptome (Schwindel, Ohnmacht, Brustschmerzen)

## 🔧 Fehlerbehebung

### Problem: "Keine Herzfrequenzdaten gefunden"

**Checkliste:**
- [ ] Haben Sie überhaupt Herzfrequenz-Messungen in Health?
- [ ] Ist es wirklich die Apple Health Export ZIP-Datei?
- [ ] Wurde der Export vollständig abgeschlossen?
- [ ] Prüfen Sie in Health-App ob Daten vorhanden sind

### Problem: App lädt sehr lange

**Lösungen:**
- Kleineren Datumsbereich wählen
- Datenpunkt-Anzahl reduzieren
- Browser-Tab alleine laufen lassen
- Lokale Installation statt Cloud

### Problem: Werte erscheinen unrealistisch

**Prüfen Sie:**
- Quelle der Messung (manche Apps sind ungenau)
- Messzeitpunkt (während Bewegung?)
- Sensor-Qualität (schlechter Hautkontakt?)
- Anomalie-Erkennung aktivieren

## 📚 Weitere Ressourcen

**Dokumentation:**
- [ANLEITUNG.md](ANLEITUNG.md) - Ausführliche Bedienungsanleitung
- [README_HERZFREQUENZ.md](README_HERZFREQUENZ.md) - Technische Dokumentation

**Herzfrequenz-Hintergrundwissen:**
- Ruhepuls und Gesundheit
- Herzfrequenz-Variabilität (HRV)
- Maximalpuls-Berechnung
- Trainingsbereiche

**Apple Health:**
- Offizielle Apple Health Dokumentation
- Health-App Benutzerhandbuch
- Datenschutz und Sicherheit

---

**Viel Erfolg bei der Analyse Ihrer Herzfrequenzdaten! ❤️**
