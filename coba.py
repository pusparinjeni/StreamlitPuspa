import streamlit as st
import pandas as pd
import numpy as np

primaryColor = "#d33682"
backgroundColor = "#002b36"
secondaryBackgroundColor = "#586e75"
textColor = "#fafafa"
font = "sans serif"


#Mengambil Data
@st.cache
def get_data():
    return pd.read_csv("botsolxhalaladded.csv")


dataready = get_data()


st.title("Surabaya Halal Directory")

st.write('Halo Arek Suroboyo? Apakah anda pecinta kuliner? Pernahkah anda berfikir kuliner yang disajikan sudah tersertifikasi halal? Sebagai seorang muslim memang suatu kebutuhan dan diwajibkan memakanan makanan dan minuman halal, baik dari bahan dan cara pengolahannya. Kalau anda penasaran kuliner yang biasanya anda makan halal atau tidak. Aplikasi ini membantu mengecek sertifikasi halal warung/restaurant/warung/bakery dan kuliner lainnya di Kota Surabaya. Aplikasi ini menggabungkan data google maps dan data SIHALAL BPJH menggunakan algoritma Jaccad Similarity.')

st.write('Anda dapat menemukan source dan dataset disini(https: // github.com/adeindriawan/inovboyo)')

#Mengurutkan berdasarkan review
st.header("Rating Warung/Restaurant di Surabaya")
values = st.slider("Rating", 1.0, 5.0, step=0.1)
dataready.round({'Rating':1})
table_rating = dataready[['Name', 'Rating']].sort_values(by=['Rating'], ascending=False)
st.table(table_rating[table_rating['Rating'] == values].style.format({"Rating": "{:.2f}"}))


#Mengurutkan berdasarkan rating
st.header("Warung yang paling banyak direview")
values2 = st.slider("Reviews", 5, 20, step=5)
#dataready['Reviews'].astype('float')
st.table(dataready[['Name', 'Reviews']].sort_values(by=['Reviews'], ascending=False).head(values2))

#Jumlah Warung per kecamatan
#st.header("Jumlah Warung per Kecamatan")
#values3 = st.slider("Jumlah", 5, 20, step=5)
#st.table(dataready[['Kecamatan', 'Name']].groupby(["Kecamatan"]).count().sort_values("Name", ascending=False).head(values3))

#Jumlah Cabang berdasarkan website
st.header("Jumlah Cabang")
values4 = st.slider("Jumlah Cabang", 5, 20, step=5)
st.table(dataready[['Website', 'Name']].groupby(
    ["Website"]).count().sort_values("Name", ascending=False).head(values4))


