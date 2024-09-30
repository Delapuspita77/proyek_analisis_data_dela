import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Include data 
combined_df = pd.read_csv('data/combined_data.csv')

# Berikan judul dashboard
st.title("Dashboard Analisis Data : E-Commerce Public Dataset by Olist")

# Convert kolom date ke datetime untuk menghindari eror
combined_df['order_purchase_timestamp'] = pd.to_datetime(combined_df['order_purchase_timestamp'])
combined_df['order_delivered_customer_date'] = pd.to_datetime(combined_df['order_delivered_customer_date'])
combined_df['order_estimated_delivery_date'] = pd.to_datetime(combined_df['order_estimated_delivery_date'])
combined_df['review_creation_date'] = pd.to_datetime(combined_df['review_creation_date'])  

# Berikan sidebar untuk filter data berdasarkan tanggal
with st.sidebar:
    st.subheader("Filter Data Berdasarkan Tanggal")
    st.caption("range tanggal : 15-09-2016 sampai 29-08-2018") # menambahkan keterangan min. date dan max. date
    start_date = st.sidebar.date_input('Mulai dari', combined_df['order_purchase_timestamp'].min().date())
    end_date = st.sidebar.date_input('Sampai dengan', combined_df['order_purchase_timestamp'].max().date())


# Filterisasi
filtered_data = combined_df[
    (combined_df['order_purchase_timestamp'] >= pd.to_datetime(start_date)) &
    (combined_df['order_purchase_timestamp'] <= pd.to_datetime(end_date))
]

# Menerapkan filter berdasarkan inputan
mask = (combined_df['order_purchase_timestamp'] >= pd.Timestamp(start_date)) & (combined_df['order_purchase_timestamp'] <= pd.Timestamp(end_date))
filtered_df = combined_df.loc[mask]

# Analisis 1 : Pola penjualan selama satu tahun terakhir (waktu bisa disesuaikan)
monthly_sales = filtered_df.groupby(filtered_df['order_purchase_timestamp'].dt.to_period('M')).agg(
    total_sales=('price', 'sum'),
    total_orders=('order_id', 'count')
).reset_index()

monthly_sales['order_purchase_timestamp'] = monthly_sales['order_purchase_timestamp'].dt.to_timestamp()

# Visualisasi berupa line chart
st.subheader("Pola Penjualan per Bulan")
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='order_purchase_timestamp', y='total_sales', marker='o', color='b', label='Total Penjualan')
plt.title('Pola Penjualan')
plt.xticks(rotation=45)
plt.xlabel('Bulan')
plt.ylabel('Total Penjualan(Rupiah)')
plt.grid(True)
plt.legend()
st.pyplot(plt)

# Analisis 2 : Kesesuaian produk tiba dengan estimasi waktu pengiriman 
delivery_counts = filtered_df['delivery_status'].value_counts()

# Visualisasi berupa pie chart
st.subheader("Kesesuaian estimasi waktu pengiriman")
plt.figure(figsize=(6, 6))
delivery_counts.plot.pie(autopct='%1.1f%%', colors=['#99ff99','#ff9999','#66b3ff'], startangle=90)
plt.title('Waktu Pengiriman')
plt.ylabel('')
st.pyplot(plt)

# Analisis 3 : Rata-rata review yang didapat
monthly_reviews = filtered_df.groupby(filtered_df['review_creation_date'].dt.to_period('M')).agg(
    avg_review_score=('review_score', 'mean')
).reset_index()

monthly_reviews['review_creation_date'] = monthly_reviews['review_creation_date'].dt.to_timestamp()

# Visualisasi berupa bar chart
st.subheader("Skor Rata-rata Review yang didapat")
plt.figure(figsize=(12, 6))
sns.barplot(data=monthly_reviews, x='review_creation_date', y='avg_review_score', color='skyblue')
plt.title('Rata-rata review')
plt.xticks(rotation=45)
plt.xlabel('Bulan')
plt.ylabel('Rata-rata Skor Review')
plt.grid(True, axis='y')
st.pyplot(plt)

