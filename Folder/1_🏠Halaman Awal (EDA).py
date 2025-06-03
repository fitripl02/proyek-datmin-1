import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="EDA")

st.title("📈 Exploratory Data Analysis")

df = pd.read_csv("data/package_tourism.csv")

st.subheader("📄 Dataset Awal")
st.dataframe(df)

st.subheader("🧮 Statistik Deskriptif")
st.write(df.describe())

# Korelasi dan visualisasi
if st.checkbox("Tampilkan Korelasi"):
    st.subheader("🔗 Korelasi antar Variabel Numerik")
    corr = df.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

# Histogram fitur
st.subheader("📊 Distribusi Kolom Numerik")
kolom = st.selectbox("Pilih kolom", df.select_dtypes(include='number').columns)
fig, ax = plt.subplots()
sns.histplot(df[kolom], kde=True, ax=ax)
st.pyplot(fig)
