import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

st.set_page_config(page_title="Pelatihan Model")

st.title("🧠 Pelatihan Model Prediksi Harga Paket Wisata")

df = pd.read_csv("data/package_tourism.csv")

# Cek kolom target
if "Price" not in df.columns:
    st.error("Kolom 'Price' tidak ditemukan dalam dataset.")
    st.stop()

# Fitur numerik
X = df.select_dtypes(include='number').drop(columns=["Price"])
y = df["Price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluasi
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)

st.subheader("📊 Evaluasi Model")
st.write(f"R² Score: {r2:.4f}")
st.write(f"RMSE: {rmse:.2f}")

# Simpan model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")
st.success("✅ Model telah disimpan ke `model/model.pkl`.")
