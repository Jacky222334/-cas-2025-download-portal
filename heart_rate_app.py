"""
Apple Health Herzfrequenz Analyse App
Streamlit-Anwendung zur Visualisierung von Apple Health Herzfrequenzdaten
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import zipfile
import tempfile
import os
from pathlib import Path

from apple_health_parser import AppleHealthParser


st.set_page_config(
    page_title="Apple Health Herzfrequenz Analyse",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #FF6B6B 0%, #EE5A6F 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #FF6B6B;
    }
    
    .info-box {
        background: #e3f2fd;
        border-left: 4px solid #2196F3;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .warning-box {
        background: #fff3e0;
        border-left: 4px solid #ff9800;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>❤️ Apple Health Herzfrequenz Analyse</h1>
    <p>Visualisierung und Analyse Ihrer Pulsdaten</p>
</div>
""", unsafe_allow_html=True)


def extract_export_xml(uploaded_zip):
    """Extrahiert export.xml aus dem hochgeladenen Apple Health ZIP"""
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(uploaded_zip, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
                
                xml_path = Path(temp_dir) / 'apple_health_export' / 'export.xml'
                if xml_path.exists():
                    return str(xml_path)
                
                xml_path = Path(temp_dir) / 'export.xml'
                if xml_path.exists():
                    return str(xml_path)
                
                for root, dirs, files in os.walk(temp_dir):
                    if 'export.xml' in files:
                        return os.path.join(root, 'export.xml')
        
        return None
    except Exception as e:
        st.error(f"Fehler beim Extrahieren: {e}")
        return None


def create_timeline_chart(df):
    """Erstellt einen Zeitverlaufs-Chart der Herzfrequenz"""
    fig = px.line(
        df,
        x='timestamp',
        y='heart_rate',
        title='Herzfrequenz im Zeitverlauf',
        labels={'timestamp': 'Zeitpunkt', 'heart_rate': 'Herzfrequenz (bpm)'},
        color_discrete_sequence=['#FF6B6B']
    )
    
    fig.update_layout(
        hovermode='x unified',
        xaxis_title='Zeitpunkt',
        yaxis_title='Herzfrequenz (bpm)',
        height=500
    )
    
    return fig


def create_daily_chart(daily_stats):
    """Erstellt einen Chart mit täglichen Durchschnittswerten"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=daily_stats['date'],
        y=daily_stats['avg_heart_rate'],
        mode='lines+markers',
        name='Durchschnitt',
        line=dict(color='#FF6B6B', width=2),
        marker=dict(size=6)
    ))
    
    fig.add_trace(go.Scatter(
        x=daily_stats['date'],
        y=daily_stats['max_heart_rate'],
        mode='lines',
        name='Maximum',
        line=dict(color='#FF9999', width=1, dash='dash'),
        opacity=0.6
    ))
    
    fig.add_trace(go.Scatter(
        x=daily_stats['date'],
        y=daily_stats['min_heart_rate'],
        mode='lines',
        name='Minimum',
        line=dict(color='#FF9999', width=1, dash='dash'),
        opacity=0.6
    ))
    
    fig.update_layout(
        title='Tägliche Herzfrequenz-Statistiken',
        xaxis_title='Datum',
        yaxis_title='Herzfrequenz (bpm)',
        hovermode='x unified',
        height=500
    )
    
    return fig


def create_hourly_distribution_chart(hourly_stats):
    """Erstellt einen Chart der Herzfrequenz-Verteilung nach Tageszeit"""
    fig = px.bar(
        hourly_stats,
        x='hour',
        y='avg_heart_rate',
        title='Durchschnittliche Herzfrequenz nach Tageszeit',
        labels={'hour': 'Uhrzeit', 'avg_heart_rate': 'Ø Herzfrequenz (bpm)'},
        color='avg_heart_rate',
        color_continuous_scale='Reds'
    )
    
    fig.update_layout(
        xaxis_title='Stunde des Tages',
        yaxis_title='Durchschnittliche Herzfrequenz (bpm)',
        height=400
    )
    
    fig.update_xaxes(dtick=1)
    
    return fig


def create_distribution_histogram(df):
    """Erstellt ein Histogramm der Herzfrequenz-Verteilung"""
    fig = px.histogram(
        df,
        x='heart_rate',
        nbins=50,
        title='Verteilung der Herzfrequenzmessungen',
        labels={'heart_rate': 'Herzfrequenz (bpm)', 'count': 'Anzahl'},
        color_discrete_sequence=['#FF6B6B']
    )
    
    fig.update_layout(
        xaxis_title='Herzfrequenz (bpm)',
        yaxis_title='Anzahl Messungen',
        height=400
    )
    
    return fig


st.markdown("""
<div class="info-box">
    <strong>ℹ️ So exportieren Sie Ihre Apple Health Daten:</strong><br>
    1. Öffnen Sie die Health-App auf Ihrem iPhone<br>
    2. Tippen Sie auf Ihr Profilbild oben rechts<br>
    3. Scrollen Sie nach unten und wählen Sie "Alle Gesundheitsdaten exportieren"<br>
    4. Die ZIP-Datei wird erstellt und kann geteilt werden<br>
    5. Laden Sie diese ZIP-Datei hier hoch
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Apple Health Export (ZIP-Datei) hochladen",
    type=['zip'],
    help="Laden Sie die exportierte ZIP-Datei aus der Apple Health App hoch"
)

if uploaded_file is not None:
    with st.spinner('Verarbeite Apple Health Daten...'):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name
        
        try:
            with zipfile.ZipFile(tmp_file_path, 'r') as zip_ref:
                temp_extract_dir = tempfile.mkdtemp()
                zip_ref.extractall(temp_extract_dir)
                
                xml_path = Path(temp_extract_dir) / 'apple_health_export' / 'export.xml'
                if not xml_path.exists():
                    xml_path = Path(temp_extract_dir) / 'export.xml'
                
                if not xml_path.exists():
                    for root, dirs, files in os.walk(temp_extract_dir):
                        if 'export.xml' in files:
                            xml_path = Path(root) / 'export.xml'
                            break
                
                if xml_path.exists():
                    parser = AppleHealthParser(str(xml_path))
                    
                    if parser.parse_file():
                        st.success('✅ Apple Health Daten erfolgreich geladen!')
                        
                        df = parser.extract_heart_rate_data()
                        
                        if not df.empty:
                            st.session_state['heart_rate_df'] = df
                            st.session_state['parser'] = parser
                            
                            st.balloons()
                        else:
                            st.warning('⚠️ Keine Herzfrequenzdaten in der Export-Datei gefunden.')
                    else:
                        st.error('❌ Fehler beim Parsen der XML-Datei.')
                else:
                    st.error('❌ export.xml nicht in der ZIP-Datei gefunden.')
        
        except Exception as e:
            st.error(f'❌ Fehler beim Verarbeiten der Datei: {e}')
        
        finally:
            try:
                os.unlink(tmp_file_path)
            except:
                pass

if 'heart_rate_df' in st.session_state and not st.session_state['heart_rate_df'].empty:
    df = st.session_state['heart_rate_df']
    parser = st.session_state['parser']
    
    st.markdown("---")
    st.markdown("## 📊 Übersicht")
    
    stats = parser.get_statistics(df)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Gesamtmessungen",
            f"{stats['total_measurements']:,}",
            help="Anzahl aller Herzfrequenzmessungen"
        )
    
    with col2:
        st.metric(
            "Ø Herzfrequenz",
            f"{stats['average_heart_rate']:.0f} bpm",
            help="Durchschnittliche Herzfrequenz über alle Messungen"
        )
    
    with col3:
        st.metric(
            "Min / Max",
            f"{stats['min_heart_rate']:.0f} / {stats['max_heart_rate']:.0f} bpm",
            help="Niedrigster und höchster gemessener Puls"
        )
    
    with col4:
        date_range = (stats['date_range']['end'] - stats['date_range']['start']).days
        st.metric(
            "Zeitraum",
            f"{date_range} Tage",
            help="Zeitspanne der Messungen"
        )
    
    st.markdown("---")
    
    with st.sidebar:
        st.markdown("## ⚙️ Einstellungen")
        
        st.markdown("### 📅 Datumsfilter")
        
        min_date = df['timestamp'].min().date()
        max_date = df['timestamp'].max().date()
        
        use_date_filter = st.checkbox("Datumsbereich einschränken", value=False)
        
        if use_date_filter:
            date_range_selected = st.date_input(
                "Zeitraum auswählen",
                value=(max_date - timedelta(days=30), max_date),
                min_value=min_date,
                max_value=max_date
            )
            
            if len(date_range_selected) == 2:
                start_date = datetime.combine(date_range_selected[0], datetime.min.time())
                end_date = datetime.combine(date_range_selected[1], datetime.max.time())
                df_filtered = parser.filter_by_date_range(df, start_date, end_date)
            else:
                df_filtered = df
        else:
            df_filtered = df
        
        st.markdown("---")
        st.markdown("### 🔍 Anomalie-Erkennung")
        
        detect_anomalies = st.checkbox("Anomalien anzeigen", value=False)
        
        if detect_anomalies:
            std_threshold = st.slider(
                "Empfindlichkeit (Standardabweichungen)",
                min_value=1.5,
                max_value=4.0,
                value=3.0,
                step=0.5,
                help="Niedrigere Werte = mehr erkannte Anomalien"
            )
            
            anomalies = parser.detect_anomalies(df_filtered, std_threshold)
            
            if not anomalies.empty:
                st.warning(f"⚠️ {len(anomalies)} Anomalien erkannt")
            else:
                st.success("✅ Keine Anomalien gefunden")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📈 Zeitverlauf",
        "📊 Tagesstatistiken",
        "⏰ Tageszeit-Analyse",
        "📋 Rohdaten"
    ])
    
    with tab1:
        st.markdown("### Herzfrequenz im Zeitverlauf")
        
        sample_size = st.slider(
            "Anzahl anzuzeigender Datenpunkte (für bessere Performance)",
            min_value=100,
            max_value=min(10000, len(df_filtered)),
            value=min(1000, len(df_filtered)),
            step=100
        )
        
        if len(df_filtered) > sample_size:
            df_display = df_filtered.sample(n=sample_size).sort_values('timestamp')
            st.info(f"ℹ️ Zeige {sample_size} von {len(df_filtered)} Datenpunkten (zufällige Stichprobe)")
        else:
            df_display = df_filtered
        
        fig_timeline = create_timeline_chart(df_display)
        st.plotly_chart(fig_timeline, use_container_width=True)
        
        if detect_anomalies and not anomalies.empty:
            st.markdown("### ⚠️ Erkannte Anomalien")
            st.dataframe(
                anomalies.style.format({
                    'heart_rate': '{:.0f} bpm',
                    'timestamp': lambda x: x.strftime('%d.%m.%Y %H:%M')
                }),
                use_container_width=True
            )
        
        st.markdown("### 📊 Verteilung der Herzfrequenz")
        fig_hist = create_distribution_histogram(df_filtered)
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with tab2:
        st.markdown("### Tägliche Herzfrequenz-Statistiken")
        
        daily_stats = parser.get_daily_statistics(df_filtered)
        
        if not daily_stats.empty:
            fig_daily = create_daily_chart(daily_stats)
            st.plotly_chart(fig_daily, use_container_width=True)
            
            st.markdown("### 📋 Tägliche Werte")
            st.dataframe(
                daily_stats.sort_values('date', ascending=False).style.format({
                    'avg_heart_rate': '{:.0f} bpm',
                    'min_heart_rate': '{:.0f} bpm',
                    'max_heart_rate': '{:.0f} bpm',
                    'measurements': '{:.0f}'
                }),
                use_container_width=True
            )
    
    with tab3:
        st.markdown("### Herzfrequenz nach Tageszeit")
        
        hourly_stats = parser.get_hourly_distribution(df_filtered)
        
        if not hourly_stats.empty:
            fig_hourly = create_hourly_distribution_chart(hourly_stats)
            st.plotly_chart(fig_hourly, use_container_width=True)
            
            st.markdown("""
            <div class="info-box">
                <strong>💡 Interpretation:</strong><br>
                • Niedriger Puls am frühen Morgen ist normal (Ruhephase)<br>
                • Höherer Puls tagsüber durch Aktivität<br>
                • Erhöhte Werte können auf körperliche Aktivität hinweisen
            </div>
            """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("### Rohdaten")
        
        st.dataframe(
            df_filtered.style.format({
                'heart_rate': '{:.0f} bpm',
                'timestamp': lambda x: x.strftime('%d.%m.%Y %H:%M:%S')
            }),
            use_container_width=True
        )
        
        csv = df_filtered.to_csv(index=False, encoding='utf-8-sig')
        st.download_button(
            label="📥 Daten als CSV exportieren",
            data=csv,
            file_name=f"herzfrequenz_daten_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

else:
    st.markdown("""
    <div class="warning-box">
        <strong>👆 Bitte laden Sie zunächst Ihre Apple Health Export-Datei hoch</strong>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### ❤️ Über diese App")
    st.markdown("""
    Diese Anwendung analysiert Ihre Herzfrequenzdaten aus Apple Health und bietet:
    
    - **Zeitverlauf**: Visualisierung Ihrer Pulswerte über die Zeit
    - **Tagesstatistiken**: Durchschnittswerte pro Tag mit Min/Max-Bereichen
    - **Tageszeit-Analyse**: Erkennung von Mustern nach Uhrzeit
    - **Anomalie-Erkennung**: Identifikation ungewöhnlicher Werte
    - **Datenexport**: Download der gefilterten Daten als CSV
    
    **Datenschutz:** Alle Daten werden lokal verarbeitet und nicht gespeichert.
    """)
