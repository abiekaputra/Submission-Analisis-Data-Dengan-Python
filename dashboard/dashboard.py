
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_data = pd.read_csv('data/day.csv')

# Custom style
sns.set_style("whitegrid")
plt.rcParams['axes.facecolor'] = '#F9F9F9'  # plot area
plt.rcParams['axes.edgecolor'] = '#CCCCCC'  # axis borders
plt.rcParams['grid.color'] = '#EDEDED'  # gridlines
plt.rcParams['font.size'] = 12  # ukuran font

# Judul
st.title('📊 Dashboard Analisis RFM dan Penggunaan Sepeda 🚴‍♂️')

# Deskripsi
st.markdown("""
Selamat datang di dasbor interaktif untuk analisis penggunaan sepeda berdasarkan musim. 
Gunakan filter di sidebar untuk melihat bagaimana cuaca dan musim mempengaruhi penggunaan sepeda!
""")

# Sidebar (Filter Interaktif Analisis Data)
st.sidebar.header('🔍 Filter Data')
st.sidebar.markdown("Gunakan filter berikut untuk menyesuaikan analisis data sesuai musim yang Anda inginkan.")
season_filter = st.sidebar.multiselect(
    'Pilih Musim',
    options=day_data['season'].unique(),
    default=day_data['season'].unique(),
    help="Pilih satu atau lebih musim untuk melihat perbandingan"
)

# Filter data Berbasis pilihan pengguna
filtered_data = day_data[day_data['season'].isin(season_filter)]

# Perhitungan Data RFM
rfm_data = filtered_data.groupby('season').agg({
    'recency': 'mean',
    'cnt': ['sum', 'mean'],
    'registered': 'sum',
    'casual': 'sum'
}).reset_index()

rfm_data.columns = ['season', 'recency', 'totalUsage', 'avgUsage', 'totalRegistered', 'totalCasual']

# Tampilan data RFM yang telah difilter
st.header('📈 Analisis RFM Berdasarkan Musim')
st.markdown("Data berikut adalah hasil analisis Recency, Frequency, dan Monetary (RFM) untuk setiap musim yang dipilih.")
st.dataframe(rfm_data.style.background_gradient(cmap='Blues'))

# Visualisasi (Segmen RFM Berdasarkan Musim)
st.header('📊 Segmen RFM Berdasarkan Musim')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='recency', data=rfm_data, color='#4B8BBE', label='Recency')
sns.barplot(x='season', y='totalUsage', data=rfm_data, color='#306998', label='Total Penggunaan (Proxy Frequency/Monetary)', alpha=0.6)
ax.set_title('Segmen RFM Berdasarkan Musim', fontsize=16, color='#333333', pad=20)
ax.set_xlabel('Musim (1 = Musim Dingin, 2 = Musim Semi, 3 = Musim Panas, 4 = Musim Gugur)', fontsize=12)
ax.set_ylabel('Nilai RFM', fontsize=12)
ax.legend(title='Metrik RFM', fontsize=10, title_fontsize=12, loc='upper right')
st.pyplot(fig)

# Visualisasi Tambahan (Pengguna Terdaftar vs Pengguna Kasual)
st.header('👥 Pengguna Terdaftar vs Pengguna Kasual Berdasarkan Musim')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='totalRegistered', data=rfm_data, color='#2E8B57', label='Pengguna Terdaftar')
sns.barplot(x='season', y='totalCasual', data=rfm_data, color='#DC143C', label='Pengguna Kasual', alpha=0.7)
ax.set_title('Total Pengguna Terdaftar vs Pengguna Kasual Berdasarkan Musim', fontsize=16, color='#333333', pad=20)
ax.set_xlabel('Musim (1 = Musim Dingin, 2 = Musim Semi, 3 = Musim Panas, 4 = Musim Gugur)', fontsize=12)
ax.set_ylabel('Jumlah Pengguna', fontsize=12)
ax.legend(title='Tipe Pengguna', fontsize=10, title_fontsize=12, loc='upper right')
st.pyplot(fig)

# Tampilan Insight
st.header('💡 Insight')
st.markdown('''
- **Musim panas (season 3)** memiliki penggunaan sepeda tertinggi, mengindikasikan puncak penggunaan selama musim ini.
- **Musim dingin (season 1)** memiliki penggunaan sepeda terendah, kemungkinan karena kondisi cuaca.
- **Pengguna terdaftar** secara konsisten lebih banyak daripada **pengguna kasual** di semua musim, tetapi pengguna kasual menunjukkan lonjakan lebih tinggi di musim panas.
- **Rata-rata recency** menurun seiring berjalannya musim, yang mungkin menunjukkan peningkatan penggunaan mendekati musim panas dan gugur.
''')

# Footer
st.markdown("""
---
📅 **Sumber data**: Dataset Penggunaan Sepeda Harian dan Jam.
""")
