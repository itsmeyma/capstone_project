import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly as py
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns




st.set_page_config(layout="wide")
st.markdown("<h1 style = 'text-align : center; color : violet; font_size : 40 px; font-family : Arial'><b>Hi! Welcome to my Capstone Project<b></h1>", unsafe_allow_html= True)

image = Image.open('happiness.jpg')
st.image(image, caption='Happiness')

st.markdown("<h1 style = 'text-align : center; color : white; font_size : 8 px; font-family : Arial'><b>Apa sih yang mempengaruhi tingkat kebahagiaan suatu negara?<b></h1>", unsafe_allow_html= True)
st.write(":orange[_Tingkat kebahagiaan suatu negara di pengaruhi oleh 6 faktor, yaitu pendapatan(GDP), kesehatan(health), dukungan social(social support), kebebasan dalam memilih tujuan hidup(freedom to make life decision), kemurahan hati(generosity) dan persepsi atas korupsi(perceptions of corruption). Kira-kira, faktor mana yang paling mempengaruhi tingkat kebahagiaan suatu negara ya?_]")
df=pd.read_csv("world_happiness1.csv")
df_sorted = df.sort_values(by='happiness_score', ascending=False)
df_top10 = df_sorted.head(10)
df_happiness = px.data.gapminder()
fig = px.bar(df_top10, x='country', y='happiness_score', labels={'y':'happiness_score'},
             hover_data=['country'],
             title='10 Happiest Country', color_discrete_sequence=['#FDCEDF'])
fig
st.markdown(":orange[_Finland telah menjadi negara dengan tingkat kebahagiaan tertinggi selama beberapa tahaun terakhir. Alasan mengapa orang Finland lebih bahagia dibanding dengan negara lain adalah karena sejumlah faktor, diantaranya ketimpangan pendapatan yang rendah, dukungan sosial yang tinggi, kebebasan untuk mengambil keputusan, dan tingkat korupsi yang rendah._]")

df1_sorted = df.sort_values(by='gdp_per_capita', ascending=False)
df1_top10 = df1_sorted.head(10)
fig1 = px.bar(df1_top10, x='country', y='gdp_per_capita', labels={'y':'gdp_per_capita'},
             hover_data=['country'],
             title='10 country with highest gdp', color_discrete_sequence=['#B3C890'])

df2_sorted = df.sort_values(by='social_support', ascending=False)
df2_top10 = df2_sorted.head(10)
fig2 = px.bar(df2_top10, x='country', y='social_support', labels={'y':'social_support'},
             hover_data=['country'],
             title='10 country with highest social support', color_discrete_sequence=['#B4E4FF'])

df3_sorted = df.sort_values(by='health_life_expectancy', ascending=False)
df3_top10 = df3_sorted.head(10)
fig3 = px.bar(df3_top10, x='country', y='health_life_expectancy', labels={'y':'health_life_expectancy'},
             hover_data=['country'],
             title='10 country with highest health life', color_discrete_sequence=['#FDF7C3'])

df4_sorted = df.sort_values(by='freedom', ascending=False)
df4_top10 = df4_sorted.head(10)
fig4 = px.bar(df4_top10, x='country', y='freedom', labels={'y':'freedom'},
             hover_data=['country'],
             title='10 country with highest freedom', color_discrete_sequence=['#D5B4B4'])

df5_sorted = df.sort_values(by='generosity', ascending=False)
df5_top10 = df5_sorted.head(10)
fig5 = px.bar(df5_top10, x='country', y='generosity', labels={'y':'generosity'},
             hover_data=['country'],
             title='10 country with highest generosity', color_discrete_sequence=['#FBC6A4'])

df6_sorted = df.sort_values(by='perceptions_of_corruption', ascending=False)
df6_top10 = df6_sorted.head(10)
fig6 = px.bar(df6_top10, x='country', y='perceptions_of_corruption', labels={'y':'perceptions_of_corruption'},
             hover_data=['country'],
             title='10 country with highest perceptions of corruption', color_discrete_sequence=['#EF4B4B'])

options = ['GDP per Capita', 'Social Support', 'Health Life Expectancy', 'Freedom', 'Generosity', 'Perceptions of Corruption']
factor_group = st.selectbox("Faktor-Faktor yang Mempengaruhi Tingkat Kebahagiaan", options, key="factor_group")
if factor_group == 'GDP per Capita':
    st.plotly_chart(fig1)
    st.caption("")
elif factor_group == 'Social Support':
    st.plotly_chart(fig2)
    st.caption("")
elif factor_group == 'Health Life Expectancy':
    st.plotly_chart(fig3)
    st.caption("")
elif factor_group == 'Freedom':
    st.plotly_chart(fig4)
    st.caption("")
elif factor_group == 'Generosity':
    st.plotly_chart(fig5)
    st.caption("")
elif factor_group == 'Perceptions of Corruption':
    st.plotly_chart(fig6)
    st.caption("")

st.markdown(":orange[_Dari hasil analisis, dari setiap factor dapat kita lihat negara mana saja yang menjadi 10 negara tertinggi yang di pengaruhi oleh factor-faktor tersebut. Nyatanya, sebagai negara dengat tingkat kebahagiaan tertinggi, Finland tidak termasuk kedalam 10 negara yang memiliki GDP tertinggi, hanya saja Finland termasuk kedalam 10 negara tertinggi yg dipengaruhi oleh social support dan freedom._]")

correlations = df[['gdp_per_capita', 'health_life_expectancy', 'social_support', 'freedom', 'generosity', 'perceptions_of_corruption', 'happiness_score']].corr()
fig11, ax = plt.subplots(figsize = (6,4))
sns.heatmap(correlations, annot=True, cmap='coolwarm', cbar=True, ax=ax, fmt=".2g")

c1,c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap Korelasi')
    st.pyplot(fig11)
with c2:
    st.subheader('Hasilnya:')
    st.markdown(':orange[_Dari hasil korelasi ini menunjukkan bahwa keenam faktor tersebut seperti pendapatan per kapita (gdp), kesehatan (health), kebebasan (freedom), kemurahan hati (generosity), dan persepsi terhadap korupsi (corruption) tetap berperan penting dalam mempengaruhi tingkat kebahagiaan suatu negara. Tetapi, hubungan sosial, solidaritas, dukungan sosial, dan kualitas interaksi sosial memiliki peran yang lebih dominan dalam mempengaruhi tingkat kebahagiaan suatu negara._]')

st.markdown(':orange[_Thank You!!_:smile:]')
st.caption('source: https://worldhappiness.report/ed/2023/')



