import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Baca dataset
df = pd.read_csv('D:\Pythonnn\Bangkit\PRSA_Data_Dongsi_20130301-20170228_baru.csv')

# Melakukan filter untuk mengubah tipe menjadi datetime
df['tanggal'] = pd.to_datetime(df[['year', 'month', 'day']])

# Melakukan filter untuk mengambil sebagian data
filtered_data = df[(df['tanggal'] >= '2016-02-01') & (df['tanggal'] <= '2017-02-28')]

# Set tanggal sebagai indeks
filtered_data.set_index('tanggal', inplace=True)

# Resampling data untuk mendapatkan rata-rata bulanan hanya untuk kolom 'PM2.5'
monthly_avg = filtered_data['PM2.5'].resample('M').mean()

# Streamlit App
st.title('Dashboard Analisis Data Udara di Dongsi')

# Tampilkan beberapa baris data
st.write('Data Udara:')
st.dataframe(df.head())

# Visualisasi rata-rata PM2.5 per bulan
st.write('Rata-rata PM2.5 per Bulan:')
fig, ax = plt.subplots(figsize=(14, 8))
sns.lineplot(x=monthly_avg.index.strftime('%Y-%m'), y=monthly_avg.values, label='PM2.5', color='blue', marker='o')
plt.title('Tren Keseluruhan Tingkat Rata-rata Bulanan PM2.5 (Februari 2016 - Februari 2017)', fontsize=16)
plt.xlabel('Tanggal', fontsize=12)
plt.ylabel('Rata-rata Tingkat PM2.5', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)  # Menambahkan rotasi pada label tanggal untuk keterbacaan
st.pyplot(fig)


#----
# Resampling data untuk mendapatkan rata-rata bulanan hanya untuk kolom 'TEMP'
monthly_avg_temp = filtered_data['TEMP'].resample('M').mean()

# Streamlit App
st.title('Dashboard Analisis Data Suhu')

# Visualisasi rata-rata suhu per bulan
st.write('Rata-rata Suhu per Bulan:')
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x=monthly_avg_temp.index.strftime('%Y-%m'), y=monthly_avg_temp.values, color='orange', marker='o')
plt.title('Rata-rata Bulanan Perubahan Suhu dari Februari 2016 hingga Februari 2017')
plt.xlabel('Tanggal')
plt.ylabel('Suhu (TEMP)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.yticks(range(0, int(max(monthly_avg_temp.values)) + 2, 2))
plt.xticks(rotation=45)  # Menambahkan rotasi pada label tanggal untuk keterbacaan
st.pyplot(fig)

#---
# Menghitung korelasi antara variabel
correlation_matrix = df[['PM2.5', 'TEMP', 'DEWP']].corr()

# Streamlit App
st.title('Analisis Korelasi dan Scatter Plot')

# Menampilkan matriks korelasi
st.write('Matriks Korelasi:')
st.dataframe(correlation_matrix)

# Scatter plot antara PM2.5 dan TEMP
st.write('Scatter Plot antara Suhu dan Tingkat PM2.5:')
fig, ax = plt.subplots(figsize=(12, 6))
sns.scatterplot(x='TEMP', y='PM2.5', data=df, alpha=0.5, color='green')  # Mengganti warna menjadi hijau
plt.title('Scatter Plot antara Suhu dan Tingkat PM2.5')
plt.xlabel('Suhu (TEMP)')
plt.ylabel('Tingkat PM2.5')
st.pyplot(fig)

#--
# Streamlit App
st.title('Scatter Plot antara Kelembaban dan Tingkat PM2.5')

# Scatter plot antara PM2.5 dan DEWP
fig, ax = plt.subplots(figsize=(12, 6))
sns.scatterplot(x='DEWP', y='PM2.5', data=df, alpha=0.5, color='purple')  # Ganti warna menjadi ungu
plt.title('Scatter Plot antara Kelembaban dan Tingkat PM2.5')
plt.xlabel('Kelembaban (DEWP)')
plt.ylabel('Tingkat PM2.5')
st.pyplot(fig)