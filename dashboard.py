import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df_customers = pd.read_csv('main_data_customers.csv')

# Streamlit Dashboard
st.title("📊 E-Commerce Dashboard")
st.sidebar.header("Filter Data")

# Filter berdasarkan kota - dengan opsi "All Cities"
cities = ['All Cities'] + list(df_customers['customer_city'].unique())
selected_city = st.sidebar.selectbox("Pilih Kota", cities)

# Filter berdasarkan provinsi
states = ['All States'] + list(df_customers['customer_state'].unique())
selected_state = st.sidebar.selectbox("Pilih Provinsi", states)

# Filter data berdasarkan pilihan di sidebar
df_filtered = df_customers.copy()

# Jika ada filter kota, sesuaikan
if selected_city != 'All Cities':
    df_filtered = df_filtered[df_filtered['customer_city'] == selected_city]

# Jika ada filter provinsi, sesuaikan
if selected_state != 'All States':
    df_filtered = df_filtered[df_filtered['customer_state'] == selected_state]

st.sidebar.write(f"🌆 Menampilkan data untuk kota **{selected_city}**" if selected_city != 'All Cities' else "🌆 Menampilkan data untuk semua kota")
st.sidebar.write(f"🏙️ Menampilkan data untuk provinsi **{selected_state}**" if selected_state != 'All States' else "🏙️ Menampilkan data untuk semua provinsi")

# Visualisasi jumlah pembeli per kota (Top 10)
st.subheader(f"🌆 Jumlah Pembeli per Kota (Top 10) - {selected_city}")
fig, ax = plt.subplots(figsize=(12, 6))
top_customer_cities = df_filtered['customer_city'].value_counts().head(10)
sns.barplot(x=top_customer_cities.index, y=top_customer_cities.values, palette='viridis', ax=ax)
ax.set_title(f'Jumlah Pembeli per Kota (Top 10) - {selected_city}')
ax.set_xlabel('Kota')
ax.set_ylabel('Jumlah Pembeli')
plt.xticks(rotation=45)
st.pyplot(fig)

# Visualisasi jumlah pembeli per provinsi (Top 10)
st.subheader(f"🏙️ Top 10 Provinsi Berdasarkan Jumlah Pembeli - {selected_state}")
fig, ax = plt.subplots(figsize=(12, 6))
top_10_customer_market = df_filtered['customer_state'].value_counts().head(10)
sns.barplot(x=top_10_customer_market.index, y=top_10_customer_market.values, palette='viridis', ax=ax)
ax.set_title(f'Top 10 Provinsi Berdasarkan Jumlah Pembeli - {selected_state}')
ax.set_xlabel('Provinsi')
ax.set_ylabel('Jumlah Pembeli')
plt.xticks(rotation=45)
st.pyplot(fig)

# Caption for data source
st.caption("📌 Data bersumber dari dataset E-Commerce Public Data")
