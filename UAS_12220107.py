#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Ujian Akhir Semester Pemrograman Komputer 
# Nafisa Kautsar
# 12220107

# import module

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import json
import pandas as pd
from PIL import Image

f = open('kode_negara_lengkap.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
df = pd.read_csv('produksi_minyak_mentah.csv')
negara=list()
for x in df['kode_negara']:
    p=0
    for y in data:
        if y['alpha-3']==x:
            p=1
            negara.append(y['name'])
            break
    if p==0:
        negara.append("N/A")
print(len(negara))
df['name'] = negara
# Closing file
f.close()
# Title
#st.title("Hello GeeksForGeeks !!!")
nama=list()
tahun=list()
st.cache(allow_output_mutation=True)
st.set_page_config(layout="wide")

st.write("UAS Pemrograman Komputer by Nafisa Kautsar NIM 12220107")
st.title("PRODUKSI MINYAK TIAP NEGARA BERDASARKAN NEGARA DAN JUMLAH PRODUKSI")
image = Image.open("oil rig.png")
st.image(image)
a_input = st.text_input("Menampilkan Grafik Produksi perTahun Pada Suatu Negara")

b_input = st.text_input("Menampilkan Grafik Produksi perNegara Pada Suatu Tahun")

c_input = st.button("Mencari Produksi Maksimum tidap negara")

d_input = st.button("Menampilkan Data Tiap Negara")


if a_input!="":
    
    for x in range(0,len(df)):
        if(df.loc[x]['name'] == a_input):
            nama.append(df.loc[x]['produksi'])
            tahun.append(df.loc[x]['tahun'])
    df1 = pd.DataFrame(dict(
        Produksi = nama,
        Tahun = tahun
        ))

    fig = px.line(        
            df1, #Data Frame
            x = "Tahun", #Columns from the data frame
            y = "Produksi",
            title = a_input
        )
    fig.update_traces(line_color = "maroon")

    st.plotly_chart(fig)
if b_input!="":
    for x in range(0,len(df)):
        if(df.loc[x]['tahun'] == int(b_input)):
            nama.append(df.loc[x]['produksi'])
            tahun.append(df.loc[x]['name'])
    df1 = pd.DataFrame(dict(
        Produksi = nama,
        nama_negara = tahun
        ))

    fig = px.line(        
            df1, #Data Frame
            y = "nama_negara", #Columns from the data frame
            x = "Produksi",
            title = b_input
        )
    fig.update_traces(line_color = "maroon")

    st.plotly_chart(fig)

if c_input:
    negara=list()
    produksi=list()
    negara.append(df.loc[0]['name'])
    produksi.append(df.loc[0]['produksi'])
    for x in range(1,len(df)):
        if df.loc[x]['name']==negara[len(negara)-1]:
            if produksi[len(produksi)-1]<df.loc[x]['produksi']:
                produksi[len(produksi)-1]=df.loc[x]['produksi']
        else:
            negara.append(df.loc[x]['name'])
            produksi.append(df.loc[x]['produksi'])
                
    df1 = pd.DataFrame(dict(
        Produksi = produksi,
        nama_negara = negara
        ))

    fig = px.line(        
            df1, #Data Frame
            x = "nama_negara", #Columns from the data frame
            y = "Produksi",
            title = b_input
        )
    fig.update_traces(line_color = "maroon")

    st.plotly_chart(fig)
if d_input:
    st.dataframe(data)




