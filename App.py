import streamlit as st

st.set_page_config(
    page_title="Dashboard Paket Wisata",
    layout="wide",
    page_icon="🌍"
)

st.title("📊 Dashboard Analisis Paket Wisata")
st.markdown("""
Selamat datang di dashboard analisis paket wisata!  
Silakan pilih halaman di sidebar:
- EDA untuk eksplorasi data
- Model untuk melatih prediktor harga
- Prediksi untuk estimasi harga berdasarkan input
""")
