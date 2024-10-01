# Proyek Analisis Data : E-Commerce Public Dataset by Olist 🎁 

Analisis ini dibuat dengan tujuan memahami pola penjualan, kesesuaian estimasi waktu pengiriman, dan analisis skor review pelanggan dengan kurun waktu tertentu sesuai dengan data yang telah tersedia.

## Fitur Utama⚡

1. Analisis pola penjualan daalam kurun waktu tertentu.
2. Analisis kesesuaian produk tiba dengan estimasi waktu pengiriman.
3. Analisis rata-rata review yang didapat.
4. Visualisasi interaktif : Pengguna dapat mengatur tanggal mulai dan akhir untuk mengetahui analisis pada waktu-waktu tertentu sesuai keinginan.

## Struktur Proyek 🔍

Proyek ini terdiri dari beberapa file dan direktori:
- `dashboard.py`: Script Python untuk menjalankan dasbor interaktif menggunakan Streamlit.
- `data/`: Direktori yang berisi semua data csv yang diperlukan
  - `combined_data.csv`: Data gabungan untuk membangun dashboard
  - `olist_order_dataset.csv`: Data pesanan yang dibuat pengguna
  - `olist_order_items_dataset.csv`: Data detail pesanan yang dibuat pengguna
  - `olist_order_reviews_dataset.csv`: Data review yang dibuat oengguna
- `notebook.ipynb`: Notebook Collabs untuk analisis mendalam dan eksplorasi data.
- `README.md`: File ini yang berisi penjelasan tentang proyek.
- `requirements.txt`: Daftar library yang diperlukan untuk menjalankan proyek
- `url.txt` : Link dashboard streamlit yang bisa langsung dibuka

## Cara Menjalankan Proyek🔓

### 1. Menjalankan file ipynb di Google Collabs

1. Buka Google Colab:
   - Kunjungi [Google Colab](https://colab.research.google.com/).

2. Buat Notebook Baru:
   - Pilih "File" > "New Notebook".

3. Unggah Dataset:
   - Anda dapat mengunggah file dataset ke Google Colab menggunakan fitur unggah file.
   - Upload data yang diperlukan (olist_order_dataset.csv, olist_order_items_dataset.csv, olist_order_reviews_dataset.csv)

4. Pasang Dependensi:
   - Instal dependensi yang diperlukan
   !pip install -r requirements.txt

### 2. Menjalankan Dasbor Streamlit
Untuk menjalankan dasbor interaktif:
1. Instal semua dependensi jika belum dilakukan:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run dashboard/dashboard.py
   ```

