# 📱 Anleitung: Apple Health Herzfrequenz-Analyse

## Schnellstart

### 1. App starten

```bash
streamlit run heart_rate_app.py
```

Die Anwendung öffnet sich automatisch im Browser unter `http://localhost:8501`

### 2. Apple Health Daten exportieren

**Auf dem iPhone:**

1. **Health-App** öffnen
2. Auf **Profilbild** (oben rechts) tippen
3. Nach unten scrollen
4. **„Alle Gesundheitsdaten exportieren"** wählen
5. Warten bis Export abgeschlossen ist (kann einige Minuten dauern)
6. ZIP-Datei speichern oder teilen

**Wichtig:** Der Export enthält ALLE Ihre Gesundheitsdaten, nicht nur Herzfrequenz. Die Datei kann mehrere hundert MB groß sein.

### 3. ZIP-Datei hochladen

1. In der Web-App auf **„Browse files"** klicken
2. Die exportierte ZIP-Datei auswählen
3. Warten während die Daten verarbeitet werden
4. Die Analyse wird automatisch angezeigt

## 📊 Funktionen im Detail

### Übersichts-Statistiken

Nach dem Upload sehen Sie sofort:
- **Gesamtmessungen**: Wie viele Herzfrequenz-Datenpunkte erfasst wurden
- **Durchschnittliche Herzfrequenz**: Ihr mittlerer Puls
- **Min/Max-Werte**: Niedrigste und höchste gemessene Herzfrequenz
- **Zeitraum**: Über wie viele Tage die Daten reichen

### Tab 1: Zeitverlauf

**Hauptdiagramm**: Zeigt Ihre Herzfrequenz über die Zeit
- Interaktiv: Zoomen durch Klicken und Ziehen
- Hover: Details zu jedem Datenpunkt
- Performance-Einstellung: Anzahl der angezeigten Punkte regulieren

**Verteilungshistogramm**: Zeigt, wie oft welche Herzfrequenzbereiche vorkommen
- Hilft normale vs. außergewöhnliche Werte zu erkennen
- Sollte normalerweise eine Glockenkurve zeigen

### Tab 2: Tagesstatistiken

**Tagesdiagramm**: 
- Durchschnittliche Herzfrequenz pro Tag
- Min/Max-Bereiche als gestrichelte Linien
- Erkennung von Trends über mehrere Tage

**Datentabelle**: 
- Detaillierte Werte für jeden Tag
- Sortierbar nach Datum
- Zeigt auch Anzahl der Messungen pro Tag

### Tab 3: Tageszeit-Analyse

**Stundendiagramm**:
- Durchschnittliche Herzfrequenz nach Uhrzeit
- Hilft bei der Erkennung von Mustern
- Typisch: Niedrig am Morgen, höher tagsüber

**Interpretation**:
- **4-7 Uhr**: Niedrigste Werte (Schlaf)
- **9-12 Uhr**: Anstieg (Aktivität beginnt)  
- **14-18 Uhr**: Oft höchste Werte (Tagesaktivität)
- **20-23 Uhr**: Abnahme (Entspannung)

### Tab 4: Rohdaten

- Vollständige Datentabelle mit allen Details
- Timestamp, Herzfrequenz, Einheit, Quelle
- **CSV-Export**: Download-Button für weitere Analysen in Excel etc.

## ⚙️ Seitenleiste: Einstellungen

### Datumsfilter

1. **„Datumsbereich einschränken"** aktivieren
2. Start- und Enddatum auswählen
3. Alle Diagramme werden automatisch aktualisiert

**Verwendung**: 
- Fokus auf bestimmte Zeiträume
- Vergleich von Wochen/Monaten
- Ausschluss von Ausreißer-Perioden

### Anomalie-Erkennung

1. **„Anomalien anzeigen"** aktivieren
2. **Empfindlichkeit** einstellen (1,5 - 4,0 Standardabweichungen)
   - Niedriger Wert = mehr Anomalien werden erkannt
   - Hoher Wert = nur extreme Ausreißer
3. Erkannte Anomalien werden in Tab 1 angezeigt

**Was sind Anomalien?**
- Werte, die statistisch ungewöhnlich sind
- Können auf intensive Aktivität hinweisen
- Oder auf Messfehler/Störungen
- Oder auf gesundheitliche Ereignisse

**Standard-Empfehlung**: 3,0 Standardabweichungen (ausgewogen)

## 💡 Tipps für die Nutzung

### Performance bei großen Datenmengen

**Problem**: Zu viele Datenpunkte machen die App langsam

**Lösung**:
1. Verwenden Sie den Datumsfilter um Zeitraum einzuschränken
2. Reduzieren Sie die Anzahl der Datenpunkte im Slider
3. Die App zeigt dann eine repräsentative Stichprobe

### Aussagekräftige Analysen

**Tipps**:
- Mindestens 7 Tage Daten für Tageszeit-Muster
- 30+ Tage für verlässliche Trends
- Mehr Messungen = genauere Statistiken

**Datenqualität**:
- Apple Watch liefert kontinuierliche Messungen
- iPhone nur gelegentliche Messungen
- Andere Apps/Geräte variieren

### Dateninterpretation

**Normale Ruhepuls-Bereiche**:
- Erwachsene: 60-100 bpm
- Sportler: 40-60 bpm
- Kinder/Jugendliche: höher

**Faktoren die den Puls beeinflussen**:
- Körperliche Aktivität (Sport, Treppensteigen)
- Stress und Emotionen
- Koffein, Alkohol, Medikamente
- Temperatur (Hitze erhöht Puls)
- Krankheit (Fieber, Infektion)
- Tageszeit (zirkadianer Rhythmus)
- Fitness-Level

## 🔧 Problemlösungen

### "Keine Herzfrequenzdaten gefunden"

**Mögliche Ursachen**:
1. Sie haben keine Herzfrequenz-Messungen in Health
2. Die ZIP-Datei ist beschädigt
3. Falsches Dateiformat hochgeladen

**Lösung**:
- Prüfen Sie in der Health-App ob Herzfrequenz-Daten vorhanden sind
- Exportieren Sie die Daten erneut
- Stellen Sie sicher, dass es eine .zip Datei ist

### ZIP-Datei lässt sich nicht hochladen

**Mögliche Ursachen**:
1. Datei zu groß (>500 MB)
2. Browser-Problem
3. Netzwerkproblem

**Lösung**:
- Schränken Sie den Export-Zeitraum ein (falls möglich)
- Versuchen Sie einen anderen Browser
- Prüfen Sie die Internet-Verbindung

### App ist langsam

**Lösungen**:
1. Reduzieren Sie die Anzahl der Datenpunkte im Slider
2. Verwenden Sie Datumsfilter
3. Schließen Sie andere Browser-Tabs
4. Mehr RAM im System verfügbar machen

### Diagramme laden nicht

**Lösungen**:
1. Seite neu laden (F5)
2. Browser-Cache leeren
3. JavaScript im Browser aktiviert?
4. Anderen Browser versuchen

## 🔒 Datenschutz & Sicherheit

### Lokale Verarbeitung

- **Keine Cloud-Speicherung**: Ihre Daten verlassen Ihren Computer nicht
- **Temporäre Verarbeitung**: Daten werden nur während der Sitzung gehalten
- **Automatische Löschung**: Nach dem Schließen sind alle Daten weg

### Empfehlungen

- Nutzen Sie die App lokal auf Ihrem Computer
- Teilen Sie die Gesundheitsdaten-ZIP nicht mit anderen
- Bei Deployment in der Cloud: Zugriff beschränken
- Regelmäßig exportierte Dateien vom Gerät löschen

## 📥 Daten exportieren

### CSV-Export

1. Tab **„Rohdaten"** öffnen
2. Button **„📥 Daten als CSV exportieren"** klicken
3. Datei wird heruntergeladen

**CSV-Datei enthält**:
- Timestamp (Datum & Uhrzeit)
- Herzfrequenz (bpm)
- Einheit
- Quelle (Gerät/App)

**Verwendung**:
- Weitere Analysen in Excel/Numbers
- Import in andere Tools
- Langzeit-Archivierung
- Teilen mit Arzt/Trainer

## 🩺 Medizinische Hinweise

**⚠️ WICHTIG - HAFTUNGSAUSSCHLUSS**

Diese App ist **KEIN medizinisches Gerät** und dient nur zu Informationszwecken:

- ❌ Keine Diagnose
- ❌ Keine Behandlungsempfehlung  
- ❌ Kein Ersatz für ärztlichen Rat
- ✅ Nur zur Information und Selbstbeobachtung

**Wann zum Arzt?**

Konsultieren Sie einen Arzt bei:
- Unregelmäßigem Herzschlag (Arrhythmie)
- Sehr hohem Ruhepuls (>100 bpm ohne Grund)
- Sehr niedrigem Puls (<40 bpm, wenn nicht Sportler)
- Plötzlichen Änderungen im Pulsmuster
- Begleitsymptomen (Schwindel, Atemnot, Brustschmerzen)

## 🆘 Support

Bei Fragen oder Problemen:

1. Diese Anleitung vollständig lesen
2. README_HERZFREQUENZ.md konsultieren
3. Fehler-Logs in der Konsole prüfen
4. GitHub Issues erstellen (falls Repository öffentlich)

## 🔄 Updates

Die App wird kontinuierlich verbessert. Prüfen Sie regelmäßig auf Updates:

```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

---

**Version**: 1.0  
**Erstellt**: Juli 2026  
**Für**: CAS 2025 Projekt
