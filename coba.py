import streamlit as st
import pandas as pd
import numpy as np

st.title('Warung di Surabaya')


#Mengambil Data
@st.cache
def get_data():
    return pd.read_csv("botsolxhalaladded.csv")


dataready = get_data()
#st.table(dataready.head())
st.table(dataready[['Name', 'Kecamatan','Rating','Reviews']].head())

#Mengurutkan berdasarkan review
st.header("Warung dengan rating tertinggi")
values = st.slider("Rating", 1.0, 5.0, step=1.0)
dataready.round({'Rating':1})
table_rating = dataready[['Name', 'Rating']].sort_values(by=['Rating'], ascending=False)
st.table(table_rating[table_rating['Rating'] == values].style.format({"Rating": "{:.2f}"}))


#Mengurutkan berdasarkan rating
st.header("Warung yang paling banyak direview")
values2 = st.slider("Reviews", 5, 20, step=5)
dataready['Reviews'].astype('float')
st.table(dataready[['Name', 'Reviews']].sort_values(by=['Reviews'], ascending=False).head(values2))

st.header("Jumlah Warung per Kecamatan")
values3 = st.slider("Jumlah", 5, 20, step=5)
st.table(dataready[['Kecamatan', 'Name']].groupby(["Kecamatan"]).count().sort_values(
    "Name", ascending=False).head(values3))
