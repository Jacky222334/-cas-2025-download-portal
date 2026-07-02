"""
Apple Health Daten Parser für Herzfrequenz-Daten
Parst export.xml aus Apple Health und extrahiert Herzfrequenzmessungen
"""

import xml.etree.ElementTree as ET
from datetime import datetime
from typing import List, Dict, Tuple
import pandas as pd
from pathlib import Path


class AppleHealthParser:
    """Parser für Apple Health Export-Dateien"""
    
    def __init__(self, xml_file_path: str):
        """
        Initialisiert den Parser mit einer Apple Health Export XML-Datei
        
        Args:
            xml_file_path: Pfad zur export.xml Datei
        """
        self.xml_file_path = xml_file_path
        self.tree = None
        self.root = None
        
    def parse_file(self) -> bool:
        """
        Lädt und parst die XML-Datei
        
        Returns:
            True bei Erfolg, False bei Fehler
        """
        try:
            self.tree = ET.parse(self.xml_file_path)
            self.root = self.tree.getroot()
            return True
        except Exception as e:
            print(f"Fehler beim Parsen der Datei: {e}")
            return False
    
    def extract_heart_rate_data(self) -> pd.DataFrame:
        """
        Extrahiert alle Herzfrequenz-Messungen aus der XML-Datei
        
        Returns:
            DataFrame mit Spalten: timestamp, heart_rate, unit, source
        """
        heart_rate_records = []
        
        if self.root is None:
            return pd.DataFrame()
        
        for record in self.root.findall(".//Record[@type='HKQuantityTypeIdentifierHeartRate']"):
            try:
                timestamp_str = record.get('startDate')
                value = float(record.get('value'))
                unit = record.get('unit', 'count/min')
                source = record.get('sourceName', 'Unbekannt')
                
                timestamp = datetime.fromisoformat(timestamp_str.replace(' +0000', ''))
                
                heart_rate_records.append({
                    'timestamp': timestamp,
                    'heart_rate': value,
                    'unit': unit,
                    'source': source
                })
            except (ValueError, AttributeError) as e:
                continue
        
        df = pd.DataFrame(heart_rate_records)
        
        if not df.empty:
            df = df.sort_values('timestamp').reset_index(drop=True)
        
        return df
    
    def get_statistics(self, df: pd.DataFrame) -> Dict:
        """
        Berechnet Statistiken über die Herzfrequenzdaten
        
        Args:
            df: DataFrame mit Herzfrequenzdaten
            
        Returns:
            Dictionary mit statistischen Kennzahlen
        """
        if df.empty:
            return {}
        
        stats = {
            'total_measurements': len(df),
            'average_heart_rate': df['heart_rate'].mean(),
            'min_heart_rate': df['heart_rate'].min(),
            'max_heart_rate': df['heart_rate'].max(),
            'median_heart_rate': df['heart_rate'].median(),
            'std_deviation': df['heart_rate'].std(),
            'date_range': {
                'start': df['timestamp'].min(),
                'end': df['timestamp'].max()
            }
        }
        
        return stats
    
    def get_daily_statistics(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Berechnet tägliche Statistiken
        
        Args:
            df: DataFrame mit Herzfrequenzdaten
            
        Returns:
            DataFrame mit täglichen Durchschnittswerten
        """
        if df.empty:
            return pd.DataFrame()
        
        df_copy = df.copy()
        df_copy['date'] = df_copy['timestamp'].dt.date
        
        daily_stats = df_copy.groupby('date').agg({
            'heart_rate': ['mean', 'min', 'max', 'count']
        }).reset_index()
        
        daily_stats.columns = ['date', 'avg_heart_rate', 'min_heart_rate', 'max_heart_rate', 'measurements']
        
        return daily_stats
    
    def get_hourly_distribution(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Analysiert die Herzfrequenz nach Tageszeit
        
        Args:
            df: DataFrame mit Herzfrequenzdaten
            
        Returns:
            DataFrame mit durchschnittlicher Herzfrequenz pro Stunde
        """
        if df.empty:
            return pd.DataFrame()
        
        df_copy = df.copy()
        df_copy['hour'] = df_copy['timestamp'].dt.hour
        
        hourly_stats = df_copy.groupby('hour').agg({
            'heart_rate': ['mean', 'count']
        }).reset_index()
        
        hourly_stats.columns = ['hour', 'avg_heart_rate', 'measurements']
        
        return hourly_stats
    
    def filter_by_date_range(self, df: pd.DataFrame, start_date: datetime, end_date: datetime) -> pd.DataFrame:
        """
        Filtert Daten nach Datumsbereich
        
        Args:
            df: DataFrame mit Herzfrequenzdaten
            start_date: Startdatum
            end_date: Enddatum
            
        Returns:
            Gefiltertes DataFrame
        """
        if df.empty:
            return pd.DataFrame()
        
        mask = (df['timestamp'] >= start_date) & (df['timestamp'] <= end_date)
        return df.loc[mask].copy()
    
    def detect_anomalies(self, df: pd.DataFrame, std_threshold: float = 3.0) -> pd.DataFrame:
        """
        Erkennt Anomalien in den Herzfrequenzdaten
        
        Args:
            df: DataFrame mit Herzfrequenzdaten
            std_threshold: Anzahl der Standardabweichungen für Anomalie-Erkennung
            
        Returns:
            DataFrame mit Anomalien
        """
        if df.empty:
            return pd.DataFrame()
        
        mean = df['heart_rate'].mean()
        std = df['heart_rate'].std()
        
        df_copy = df.copy()
        df_copy['is_anomaly'] = (
            (df_copy['heart_rate'] < mean - std_threshold * std) |
            (df_copy['heart_rate'] > mean + std_threshold * std)
        )
        
        anomalies = df_copy[df_copy['is_anomaly']].copy()
        
        return anomalies[['timestamp', 'heart_rate', 'source']]
