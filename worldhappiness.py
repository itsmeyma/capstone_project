import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly as py
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns




st.set_page_config(layout="wide")
st.markdown("<h1 style = 'text-align : center; color : violet; font_size : 40 px; font-family : Arial'><b>Analisis Faktor-Faktor Yang Mempengaruhi Tingkat Kebahagiaan Suatu Negara<b></h1>", unsafe_allow_html= True)

image = Image.open('happiness.jpg')
st.image(image, caption='Happiness')
st.write(":blue[_Fun Fact! Tingkat kebahagiaan penduduk memiliki dampak yang signifikan dalam berbagai aspek kehidupan. Beberapa fun fact tentang relevansi antara tingkat kebahagiaan suatu negara dengan impact yang diberikan adalah:_]")
st.write(":blue[_1. Produktivitas lebih tinggi_]")
st.write(":blue[_2. Kesehatan yang lebih baik_]")
st.write(":blue[_3. Hubungan yang lebih positif_]")
st.write(":blue[_4. Kemajuan Ekonomi_]")
st.write(":blue[_5. Keberlanjutan dan kualitas hidup_]")
st.write(":blue[_6. Turis dan migrasi_]")
st.write(":blue[_Fun fact ini menunjukkan bahwa tingkat kebahagiaan suatu negara memiliki dampak yang luas dan penting dalam berbagai aspek kehidupan. Memperhatikan kebahagiaan penduduk dapat berkontribusi pada pembangunan sosial, ekonomi, dan kualitas hidup yang lebih baik._]")

st.markdown("<h1 style = 'text-align : center; color : violet; font_size : 8 px; font-family : Arial'><b>Jadi, apa sih yang mempengaruhi tingkat kebahagiaan suatu negara?<b></h1>", unsafe_allow_html= True)
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

st.markdown(":orange[_Dari hasil analisis, dari setiap faktor dapat kita lihat negara mana saja yang menjadi 10 negara tertinggi yang di pengaruhi oleh faktor-faktor tersebut. Nyatanya, sebagai negara dengat tingkat kebahagiaan tertinggi, Finland tidak termasuk kedalam 10 negara yang memiliki GDP tertinggi, hanya saja Finland termasuk kedalam 10 negara tertinggi yg dipengaruhi oleh social support dan freedom._]")
st.markdown(":orange[_Apakah terdapat korelasi antara faktor-faktor tertentu dengan tingkat kebahagiaan? Faktor apa yang paling mempengaruhi tingkat kebahagiaan?_]")
correlations = df[['gdp_per_capita', 'health_life_expectancy', 'social_support', 'freedom', 'generosity', 'perceptions_of_corruption', 'happiness_score']].corr()
fig11, ax = plt.subplots(figsize = (6,4))
sns.heatmap(correlations, annot=True, cmap='coolwarm', cbar=True, ax=ax, fmt=".2g")

c1,c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap Korelasi')
    st.pyplot(fig11)
with c2:
    st.subheader('Hasilnya:')
    st.markdown(':orange[_Dari hasil korelasi ini menunjukkan bahwa keenam faktor tersebut seperti pendapatan per kapita (gdp), kesehatan (health), kebebasan (freedom), kemurahan hati (generosity), dan persepsi terhadap korupsi (corruption) berkolerasi dengan tingkat kebahagiaan, dan faktor-faktor tersebut tetap berperan penting dalam mempengaruhi tingkat kebahagiaan suatu negara. Tetapi, hubungan sosial, solidaritas, dukungan sosial, dan kualitas interaksi sosial memiliki peran yang lebih dominan dalam mempengaruhi tingkat kebahagiaan suatu negara._]')
st.write(":blue[_Berikut ini beberapa rekomendasi untuk meningkatkan tingkat kebahagiaan negara:_]")
st.write(":blue[_1. Investasi dalam Kualitas Pendidikan: Meningkatkan akses dan kualitas pendidikan dapat memberikan dampak positif pada kebahagiaan masyarakat. Fokus pada pendidikan yang inklusif, relevan, dan berkualitas dapat membantu individu mencapai potensi penuh mereka dan meningkatkan kesejahteraan secara keseluruhan._]")
st.write(":blue[_2. Perhatian pada Kesejahteraan Mental: Memberikan perhatian yang lebih besar pada kesehatan mental adalah langkah penting untuk meningkatkan kebahagiaan suatu negara. Memperluas akses ke layanan kesehatan mental, mengurangi stigma, dan meningkatkan kesadaran tentang pentingnya kesehatan mental dapat membantu individu merasa lebih bahagia dan seimbang._]")
st.write(":blue[_3. Penguatan Jaringan Sosial: Membangun dan memperkuat jaringan sosial dapat berdampak positif pada kebahagiaan masyarakat. Inisiatif untuk mempromosikan interaksi sosial yang positif, dukungan sosial, dan solidaritas dapat menciptakan lingkungan sosial yang lebih sehat dan mendukung._]")
st.write(":blue[_4. Pembangunan Ekonomi yang Inklusif: Meningkatkan kesetaraan ekonomi dan menciptakan peluang kerja yang adil dapat berkontribusi pada kebahagiaan suatu negara. Kebijakan yang mendukung pembangunan ekonomi inklusif, pengurangan kemiskinan, perlindungan tenaga kerja, dan distribusi yang lebih adil dapat meningkatkan kesejahteraan dan kebahagiaan masyarakat._]")
st.write(":blue[_5. Partisipasi Politik dan Kebebasan: Mendorong partisipasi politik yang inklusif, kebebasan berbicara, dan akses terhadap hak-hak asasi manusia juga dapat mempengaruhi kebahagiaan suatu negara. Masyarakat yang merasa memiliki pengaruh dan otonomi dalam pembuatan keputusan dapat merasa lebih bahagia dan terlibat secara aktif dalam pembangunan negara._]")
st.write(":blue[_6. Keseimbangan Kerja dan Kehidupan Pribadi: Membangun lingkungan kerja yang seimbang dan mendukung kehidupan pribadi yang sehat dapat meningkatkan kebahagiaan individu. Kebijakan yang mempromosikan fleksibilitas kerja, cuti yang memadai, dan kesetimbangan antara pekerjaan dan kehidupan pribadi dapat membantu masyarakat mencapai keseimbangan yang lebih baik._]")
st.write(":blue[_Rekomendasi-rekomendasi ini dapat menjadi panduan untuk memperbaiki dan meningkatkan kebahagiaan suatu negara. Namun, setiap negara memiliki konteks dan tantangan yang berbeda, sehingga solusi yang efektif harus disesuaikan dengan kondisi masing-masing negara._]")
st.markdown(':orange[_Thank You!!_:smile:]')
st.caption('source: https://worldhappiness.report/ed/2023/')



