"""
CAS 2025 Dashboard
Zentrales Dashboard für Dokumenten-Download und Gesundheitsdaten-Analyse
"""

import streamlit as st
import os
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import zipfile
import tempfile

from apple_health_parser import AppleHealthParser


st.set_page_config(
    page_title="CAS 2025 Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .nav-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        cursor: pointer;
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }
    
    .nav-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
        border-color: #667eea;
    }
    
    .metric-card {
        background: white;
        border: 2px solid #e9ecef;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    .info-box {
        background: #e3f2fd;
        border-left: 4px solid #2196F3;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .success-box {
        background: #e8f5e9;
        border-left: 4px solid #4caf50;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .warning-box {
        background: #fff3e0;
        border-left: 4px solid #ff9800;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .paper-card {
        background: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .paper-card:hover {
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        transform: translateX(5px);
    }
    
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Session State Initialisierung
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Sidebar Navigation
with st.sidebar:
    st.markdown("# 🎓 Navigation")
    
    if st.button("🏠 Startseite", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()
    
    if st.button("❤️ Herzfrequenz-Analyse", use_container_width=True):
        st.session_state.page = 'heart_rate'
        st.rerun()
    
    if st.button("📚 Dokumenten-Download", use_container_width=True):
        st.session_state.page = 'documents'
        st.rerun()
    
    st.markdown("---")
    
    st.markdown("### ℹ️ Information")
    st.markdown(f"""
    **Aktuelle Seite:**  
    {st.session_state.page.replace('_', ' ').title()}
    
    **Datum:**  
    {datetime.now().strftime('%d.%m.%Y')}
    
    **Zeit:**  
    {datetime.now().strftime('%H:%M')} Uhr
    """)


# ==================== STARTSEITE ====================
def show_home():
    st.markdown("""
    <div class="main-header">
        <h1>🎓 CAS 2025 Dashboard</h1>
        <p>Gesundheitsdaten-Analyse & Dokumenten-Portal</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## Willkommen im CAS 2025 Dashboard")
    st.markdown("Wählen Sie eine Funktion aus:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="nav-card">
            <h2>❤️ Herzfrequenz-Analyse</h2>
            <p>Analysieren Sie Ihre Apple Health Pulsdaten:</p>
            <ul>
                <li>Zeitverlauf-Visualisierung</li>
                <li>Tagesstatistiken</li>
                <li>Tageszeit-Analyse</li>
                <li>Anomalie-Erkennung</li>
                <li>CSV-Export</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Zur Herzfrequenz-Analyse →", key="nav_hr", use_container_width=True):
            st.session_state.page = 'heart_rate'
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="nav-card">
            <h2>📚 Dokumenten-Download</h2>
            <p>Laden Sie CAS-Dokumente herunter:</p>
            <ul>
                <li>Non-Binary Teacher Dokumentation</li>
                <li>CAS Programm 2025</li>
                <li>Transidentität Präsentation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Zum Dokumenten-Portal →", key="nav_docs", use_container_width=True):
            st.session_state.page = 'documents'
            st.rerun()
    
    st.markdown("---")
    
    # Übersichts-Statistiken
    st.markdown("## 📊 Übersicht")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Verfügbare Dokumente",
            "3",
            help="Anzahl der CAS-Dokumente zum Download"
        )
    
    with col2:
        if 'heart_rate_df' in st.session_state:
            st.metric(
                "Herzfrequenz-Messungen",
                f"{len(st.session_state['heart_rate_df']):,}",
                help="Aktuell geladene Herzfrequenzdaten"
            )
        else:
            st.metric(
                "Herzfrequenz-Messungen",
                "Keine Daten",
                help="Laden Sie Apple Health Daten hoch"
            )
    
    with col3:
        st.metric(
            "Funktionen",
            "2",
            help="Hauptfunktionen des Dashboards"
        )
    
    st.markdown("---")
    
    # Quick Links
    st.markdown("## 🔗 Schnellzugriff")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-box">
            <strong>📖 Dokumentation</strong><br>
            • <a href="#" target="_self">README</a><br>
            • <a href="#" target="_self">Anleitung</a><br>
            • <a href="#" target="_self">Beispiele</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-box">
            <strong>✅ Status</strong><br>
            • System: Online<br>
            • Parser: Bereit<br>
            • Dokumente: Verfügbar
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="warning-box">
            <strong>💡 Hinweis</strong><br>
            • Datenschutz beachten<br>
            • Lokale Verarbeitung<br>
            • Keine Speicherung
        </div>
        """, unsafe_allow_html=True)


# ==================== HERZFREQUENZ-ANALYSE ====================
def show_heart_rate():
    st.markdown("""
    <div class="main-header">
        <h1>❤️ Apple Health Herzfrequenz-Analyse</h1>
        <p>Visualisierung und Analyse Ihrer Pulsdaten</p>
    </div>
    """, unsafe_allow_html=True)
    
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
        
        # Sidebar Filter
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
        
        # Visualisierungen
        tab1, tab2, tab3 = st.tabs(["📈 Zeitverlauf", "📊 Tagesstatistiken", "📋 Rohdaten"])
        
        with tab1:
            st.markdown("### Herzfrequenz im Zeitverlauf")
            
            sample_size = min(1000, len(df_filtered))
            
            if len(df_filtered) > sample_size:
                df_display = df_filtered.sample(n=sample_size).sort_values('timestamp')
            else:
                df_display = df_filtered
            
            fig = px.line(
                df_display,
                x='timestamp',
                y='heart_rate',
                title='Herzfrequenz im Zeitverlauf',
                labels={'timestamp': 'Zeitpunkt', 'heart_rate': 'Herzfrequenz (bpm)'},
                color_discrete_sequence=['#FF6B6B']
            )
            
            fig.update_layout(
                hovermode='x unified',
                height=500
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            st.markdown("### Tägliche Herzfrequenz-Statistiken")
            
            daily_stats = parser.get_daily_statistics(df_filtered)
            
            if not daily_stats.empty:
                fig = go.Figure()
                
                fig.add_trace(go.Scatter(
                    x=daily_stats['date'],
                    y=daily_stats['avg_heart_rate'],
                    mode='lines+markers',
                    name='Durchschnitt',
                    line=dict(color='#FF6B6B', width=2),
                ))
                
                fig.update_layout(
                    title='Tägliche Herzfrequenz-Statistiken',
                    xaxis_title='Datum',
                    yaxis_title='Herzfrequenz (bpm)',
                    hovermode='x unified',
                    height=500
                )
                
                st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            st.markdown("### Rohdaten")
            
            st.dataframe(
                df_filtered.head(100),
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


# ==================== DOKUMENTEN-PORTAL ====================
def show_documents():
    st.markdown("""
    <div class="main-header">
        <h1>📚 CAS 2025 Dokumenten-Portal</h1>
        <p>Download von CAS-Dokumenten</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## 📋 Verfügbare Dokumente")
    st.markdown("Klicken Sie auf den Download-Button, um die gewünschten Dokumente herunterzuladen.")
    
    # Funktion für Dateigröße
    def get_file_size(file_path):
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            if size < 1024:
                return f"{size} B"
            elif size < 1024*1024:
                return f"{size/1024:.0f} KB"
            else:
                return f"{size/(1024*1024):.1f} MB"
        return "Unbekannt"
    
    # Dokumentenliste
    files = [
        {
            'name': 'Non-Binary Teacher Dokumentation',
            'filename': 'cas_nonbinaryteacher.pdf',
            'description': 'Dokumentation zum Thema Non-Binary Teacher',
            'emoji': '📄'
        },
        {
            'name': 'CAS Programm 2025',
            'filename': 'CAS_Programm 2025.docx',
            'description': 'Vollständiges Programm für den CAS 2025 Kurs',
            'emoji': '📝'
        },
        {
            'name': 'Transidentität Teil 1 - CAS Präsentation',
            'filename': 'Transidentität_Teil1_CAS_22112024v3.pptx',
            'description': 'Präsentation zum Thema Transidentität (Teil 1)',
            'emoji': '📊'
        }
    ]
    
    for file_info in files:
        file_path = file_info['filename']
        file_size = get_file_size(file_path)
        file_extension = Path(file_path).suffix.upper()[1:]
        
        st.markdown(f"""
        <div class="paper-card">
            <h3>{file_info['emoji']} {file_info['name']}</h3>
            <p>{file_info['description']}</p>
            <p><strong>Format:</strong> {file_extension} | <strong>Größe:</strong> {file_size}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if os.path.exists(file_path):
            with open(file_path, "rb") as file:
                st.download_button(
                    label=f"📥 Download {file_extension}",
                    data=file,
                    file_name=file_info['filename'],
                    mime="application/octet-stream",
                    key=f"download_{file_info['filename']}",
                    use_container_width=True
                )
        else:
            st.error(f"❌ Datei '{file_path}' nicht gefunden!")
        
        st.markdown("<br>", unsafe_allow_html=True)


# ==================== HAUPTLOGIK ====================
if st.session_state.page == 'home':
    show_home()
elif st.session_state.page == 'heart_rate':
    show_heart_rate()
elif st.session_state.page == 'documents':
    show_documents()
