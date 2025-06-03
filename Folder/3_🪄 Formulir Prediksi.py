import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="Form Prediksi")

st.title("🔮 Prediksi Harga Paket Wisata")

# Load model
try:
    model = joblib.load("model/model.pkl")
except:
    st.error("Model belum tersedia. Silakan latih model terlebih dahulu.")
    st.stop()

# Load data untuk mengambil fitur
df = pd.read_csv("data/package_tourism.csv")
fitur_model = df.select_dtypes(include='number').drop(columns=["Price"]).columns

st.subheader("📝 Masukkan Nilai Fitur")

user_input = []
for fitur in fitur_model:
    nilai = st.number_input(f"Masukkan nilai untuk '{fitur}'", min_value=0.0, value=1.0)
    user_input.append(nilai)

if st.button("Prediksi"):
    input_array = np.array([user_input])
    hasil = model.predict(input_array)[0]
    st.success(f"💰 Estimasi Harga Paket Wisata: Rp {hasil:,.0f}")
