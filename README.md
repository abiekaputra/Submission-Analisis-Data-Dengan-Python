# Dasbor Analisis Penggunaan Sepeda 🚴‍♂️

Proyek ini menyediakan sebuah dasbor interaktif yang dibuat menggunakan **Streamlit**, bertujuan untuk menganalisis dataset penggunaan sepeda. Fokus utama analisis ini adalah pada **RFM (Recency, Frequency, Monetary)** dan pengaruh **kategori kelembapan** terhadap jumlah penyewaan sepeda.

## Fitur Utama 🚀

- **Analisis RFM**: Mengukur perilaku pelanggan berdasarkan waktu interaksi terakhir (Recency), frekuensi interaksi (Frequency), dan jumlah penyewaan (Monetary).
- **Analisis Kelembapan**: Menunjukkan bagaimana kategori kelembapan (kering, normal, lembap) memengaruhi jumlah penggunaan sepeda.
- **Visualisasi Interaktif**: Memungkinkan pengguna untuk memfilter data berdasarkan musim dan mengamati pola penggunaan sepeda.

## Struktur Proyek 📂

Proyek ini terdiri dari beberapa file dan direktori:
- `dashboard.py`: Script Python untuk menjalankan dasbor interaktif menggunakan Streamlit.
- `data/`: Direktori yang berisi data penggunaan sepeda harian dan jam.
  - `day.csv`: Data penggunaan sepeda harian.
  - `hour.csv`: Data penggunaan sepeda per jam.
- `notebook.ipynb`: Notebook Jupyter untuk analisis mendalam dan eksplorasi data.
- `README.md`: File ini yang berisi penjelasan tentang proyek.
- `requirements.txt`: Daftar pustaka Python yang diperlukan untuk menjalankan proyek.

## Cara Menjalankan Proyek 💻

### 1. Menjalankan Jupyter Notebook
Untuk menjalankan analisis pada notebook Jupyter:
1. Pastikan dependensi sudah terpasang menggunakan `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
2. Buka Jupyter Notebook:
   ```bash
   jupyter notebook notebook.ipynb
   ```

### 2. Menjalankan Dasbor Streamlit
Untuk menjalankan dasbor interaktif:
1. Instal semua dependensi jika belum dilakukan:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run dashboard.py
   ```"# Submission_Analisis_Data_Dengan_Python" 
"# Submission-Belajar-Analisis-Data-dengan-Python" 
