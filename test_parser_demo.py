"""
Demo-Skript zum Testen des Apple Health Parsers
Zeigt grundlegende Funktionalität ohne echte Daten
"""

from apple_health_parser import AppleHealthParser
import pandas as pd
from datetime import datetime, timedelta
import random

def create_sample_data():
    """
    Erstellt Beispiel-Herzfrequenzdaten für Demo-Zwecke
    """
    print("📊 Erstelle Beispiel-Herzfrequenzdaten...\n")
    
    # Simuliere 7 Tage Daten
    base_date = datetime.now() - timedelta(days=7)
    heart_rates = []
    
    for day in range(7):
        for hour in range(24):
            # Realistisches Herzfrequenz-Muster über den Tag
            if 0 <= hour < 6:  # Nacht: niedrigerer Puls
                base_hr = random.randint(55, 65)
            elif 6 <= hour < 9:  # Morgen: ansteigend
                base_hr = random.randint(65, 80)
            elif 9 <= hour < 18:  # Tag: aktiver
                base_hr = random.randint(75, 95)
            elif 18 <= hour < 22:  # Abend: Sport/Aktivität möglich
                base_hr = random.randint(70, 120)
            else:  # Vor Schlafenszeit
                base_hr = random.randint(65, 75)
            
            # Mehrere Messungen pro Stunde
            for _ in range(random.randint(1, 5)):
                timestamp = base_date + timedelta(days=day, hours=hour, minutes=random.randint(0, 59))
                heart_rate = base_hr + random.randint(-5, 5)
                
                heart_rates.append({
                    'timestamp': timestamp,
                    'heart_rate': heart_rate,
                    'unit': 'count/min',
                    'source': 'Apple Watch' if random.random() > 0.1 else 'iPhone'
                })
    
    df = pd.DataFrame(heart_rates)
    df = df.sort_values('timestamp').reset_index(drop=True)
    
    print(f"✅ {len(df)} Beispiel-Messungen erstellt\n")
    return df


def demo_statistics(df):
    """Zeigt Grundstatistiken"""
    print("=" * 60)
    print("📈 GRUNDSTATISTIKEN")
    print("=" * 60)
    
    print(f"Gesamtmessungen:        {len(df):>8,}")
    print(f"Durchschnittspuls:      {df['heart_rate'].mean():>8.1f} bpm")
    print(f"Minimaler Puls:         {df['heart_rate'].min():>8.0f} bpm")
    print(f"Maximaler Puls:         {df['heart_rate'].max():>8.0f} bpm")
    print(f"Median:                 {df['heart_rate'].median():>8.0f} bpm")
    print(f"Standardabweichung:     {df['heart_rate'].std():>8.2f} bpm")
    print(f"Zeitraum:               {df['timestamp'].min().strftime('%d.%m.%Y')} bis {df['timestamp'].max().strftime('%d.%m.%Y')}")
    print()


def demo_daily_stats(df):
    """Zeigt tägliche Statistiken"""
    print("=" * 60)
    print("📅 TÄGLICHE STATISTIKEN")
    print("=" * 60)
    
    df_copy = df.copy()
    df_copy['date'] = df_copy['timestamp'].dt.date
    
    daily = df_copy.groupby('date').agg({
        'heart_rate': ['mean', 'min', 'max', 'count']
    }).reset_index()
    
    daily.columns = ['Datum', 'Ø Puls', 'Min', 'Max', 'Messungen']
    
    print(daily.to_string(index=False))
    print()


def demo_hourly_distribution(df):
    """Zeigt stündliche Verteilung"""
    print("=" * 60)
    print("⏰ HERZFREQUENZ NACH TAGESZEIT")
    print("=" * 60)
    
    df_copy = df.copy()
    df_copy['hour'] = df_copy['timestamp'].dt.hour
    
    hourly = df_copy.groupby('hour')['heart_rate'].agg(['mean', 'count']).reset_index()
    
    print(f"{'Stunde':<8} {'Ø Puls':<12} {'Messungen':<12} {'Visualisierung'}")
    print("-" * 60)
    
    for _, row in hourly.iterrows():
        hour = int(row['hour'])
        avg_hr = row['mean']
        count = int(row['count'])
        
        # Einfache Balkenvisualisierung
        bar_length = int((avg_hr - 50) / 2)  # Skalierung für Visualisierung
        bar = "█" * bar_length
        
        print(f"{hour:02d}:00    {avg_hr:>6.1f} bpm   {count:>4}         {bar}")
    
    print()


def demo_anomalies(df):
    """Zeigt Anomalie-Erkennung"""
    print("=" * 60)
    print("🔍 ANOMALIE-ERKENNUNG")
    print("=" * 60)
    
    mean = df['heart_rate'].mean()
    std = df['heart_rate'].std()
    threshold = 2.5
    
    df_copy = df.copy()
    df_copy['is_anomaly'] = (
        (df_copy['heart_rate'] < mean - threshold * std) |
        (df_copy['heart_rate'] > mean + threshold * std)
    )
    
    anomalies = df_copy[df_copy['is_anomaly']]
    
    print(f"Schwellenwert:          {threshold} Standardabweichungen")
    print(f"Normale Range:          {mean - threshold * std:.1f} - {mean + threshold * std:.1f} bpm")
    print(f"Gefundene Anomalien:    {len(anomalies)}")
    print()
    
    if len(anomalies) > 0:
        print("Beispiel-Anomalien:")
        print("-" * 60)
        for _, row in anomalies.head(5).iterrows():
            timestamp_str = row['timestamp'].strftime('%d.%m.%Y %H:%M')
            hr = row['heart_rate']
            deviation = abs(hr - mean) / std
            print(f"{timestamp_str}  |  {hr:>3.0f} bpm  |  {deviation:.1f}σ vom Mittelwert")
    
    print()


def demo_sources(df):
    """Zeigt Datenquellen-Verteilung"""
    print("=" * 60)
    print("📱 DATENQUELLEN")
    print("=" * 60)
    
    sources = df['source'].value_counts()
    
    for source, count in sources.items():
        percentage = (count / len(df)) * 100
        bar_length = int(percentage / 2)
        bar = "█" * bar_length
        print(f"{source:<20} {count:>6} ({percentage:>5.1f}%)  {bar}")
    
    print()


def main():
    """Hauptfunktion für Demo"""
    print("\n" + "=" * 60)
    print("❤️  APPLE HEALTH PARSER - DEMO")
    print("=" * 60)
    print()
    
    # Beispieldaten erstellen
    df = create_sample_data()
    
    # Verschiedene Analysen demonstrieren
    demo_statistics(df)
    demo_daily_stats(df)
    demo_hourly_distribution(df)
    demo_anomalies(df)
    demo_sources(df)
    
    print("=" * 60)
    print("✅ Demo abgeschlossen!")
    print("=" * 60)
    print()
    print("💡 Tipp: Verwenden Sie 'streamlit run heart_rate_app.py'")
    print("   um echte Apple Health Daten zu analysieren.")
    print()


if __name__ == "__main__":
    main()
