import streamlit as st
import os
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="CAS 2025 - Paper Download",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .paper-card {
        background: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    .file-info {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 0.5rem 0;
    }
    
    .file-type {
        background: #e3f2fd;
        color: #1976d2;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    .file-size {
        color: #666;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🎓 CAS 2025</h1>
    <p>Dokumenten-Download Portal</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## 📋 Verfügbare Dokumente")
st.markdown("Klicken Sie auf den Download-Button, um die gewünschten Dokumente herunterzuladen.")

# Function to get file size in readable format
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

# Function to get file type emoji
def get_file_emoji(extension):
    emoji_map = {
        '.pdf': '📄',
        '.docx': '📝',
        '.pptx': '📊',
        '.doc': '📝',
        '.ppt': '📊'
    }
    return emoji_map.get(extension.lower(), '📄')

# List of available files
files = [
    {
        'name': 'Non-Binary Teacher Dokumentation',
        'filename': 'cas_nonbinaryteacher.pdf',
        'description': 'Dokumentation zum Thema Non-Binary Teacher'
    },
    {
        'name': 'CAS Programm 2025',
        'filename': 'CAS_Programm 2025.docx',
        'description': 'Vollständiges Programm für den CAS 2025 Kurs'
    },
    {
        'name': 'Transidentität Teil 1 - CAS Präsentation',
        'filename': 'Transidentität_Teil1_CAS_22112024v3.pptx',
        'description': 'Präsentation zum Thema Transidentität (Teil 1)'
    }
]

# Display files in columns
col1, col2 = st.columns([2, 1])

for file_info in files:
    file_path = file_info['filename']
    file_extension = Path(file_path).suffix
    file_emoji = get_file_emoji(file_extension)
    file_size = get_file_size(file_path)
    
    with st.container():
        st.markdown(f"""
        <div class="paper-card">
            <h3>{file_emoji} {file_info['name']}</h3>
            <p>{file_info['description']}</p>
            <div class="file-info">
                <span class="file-type">{file_extension.upper()[1:]}</span>
                <span class="file-size">{file_size}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Download button
        if os.path.exists(file_path):
            with open(file_path, "rb") as file:
                btn = st.download_button(
                    label=f"📥 Download {file_extension.upper()[1:]}",
                    data=file,
                    file_name=file_info['filename'],
                    mime="application/octet-stream",
                    key=f"download_{file_info['filename']}",
                    use_container_width=True
                )
        else:
            st.error(f"❌ Datei '{file_path}' nicht gefunden!")
        
        st.markdown("---")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>🎓 Alle Dokumente sind für den CAS 2025 Kurs verfügbar.</p>
    <p><small>Erstellt mit Streamlit</small></p>
</div>
""", unsafe_allow_html=True)

# Sidebar with additional info
with st.sidebar:
    st.markdown("## ℹ️ Information")
    st.markdown("""
    **Verfügbare Dateiformate:**
    - 📄 PDF Dokumente
    - 📝 Word Dokumente (.docx)
    - 📊 PowerPoint Präsentationen (.pptx)
    
    **Download-Hinweise:**
    - Klicken Sie auf den Download-Button
    - Die Datei wird automatisch heruntergeladen
    - Überprüfen Sie Ihren Download-Ordner
    """)
    
    st.markdown("---")
    st.markdown("**📊 Statistiken:**")
    available_files = sum(1 for f in files if os.path.exists(f['filename']))
    st.metric("Verfügbare Dokumente", available_files)
    
    total_size = sum(os.path.getsize(f['filename']) for f in files if os.path.exists(f['filename']))
    st.metric("Gesamtgröße", f"{total_size/(1024*1024):.1f} MB") 