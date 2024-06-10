import streamlit as st
import time

LG = "https://ssl.gstatic.com/onebox/media/sports/logos/3NqgO_dpTThWu3KBf600tg_48x48.png"
KT = "https://ssl.gstatic.com/onebox/media/sports/logos/LUZj3ojt_H6lYisolvQ2pg_48x48.png"
SSG = "https://ssl.gstatic.com/onebox/media/sports/logos/171JeGI-4meYHLIoUPjerQ_48x48.png"
NC =  "https://ssl.gstatic.com/onebox/media/sports/logos/dDCbStDchWQktsZf2swYyA_48x48.png"
두산 = "https://ssl.gstatic.com/onebox/media/sports/logos/AP_sE5nmR8ckhs_zEhDzEg_48x48.png"
KIA = "https://ssl.gstatic.com/onebox/media/sports/logos/psd7z7tnBo7SD8f_Fxs-yg_48x48.png"
롯데 = "https://ssl.gstatic.com/onebox/media/sports/logos/cGrvIuBYzj4D6KFLPV1MBg_48x48.png"
삼성 = "https://ssl.gstatic.com/onebox/media/sports/logos/c_Jn4jW-NOwRtnGE7uQRAA_48x48.png"
한화 = "https://ssl.gstatic.com/onebox/media/sports/logos/pq5JUk7H0b6KX5Wi8M0xbA_48x48.png"
키움 = "https://ssl.gstatic.com/onebox/media/sports/logos/BXbvDpPIJZ_HpPL4qikxNg_48x48.png"

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.image(KIA)
with col2:
    st.image('https://st4.depositphotos.com/1404656/30086/v/450/depositphotos_300867228-stock-illustration-versus-sign-black-and-white.jpg')
with col3:
    st.image(KT)

col1, col2 = st.columns(2)

with col1:
    st.subheader('원본 영상')
    st.image('https://github.com/subninggg/streamlit/blob/main/video_gif/ge_safe2.gif?raw=true')

with col2:
    st.subheader('분석 영상')
    st.image('https://github.com/subninggg/streamlit/blob/main/hiera_gif/ge_safe2_hiera.gif?raw=true')

progress_text = "Please wait..."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

st.success('SAFE')

st.subheader('')
st.subheader('분석 과정')
st.image('https://raw.githubusercontent.com/subninggg/streamlit/main/hiera_image/ge_safe2_hiera.png')

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.link_button("다른 영상 보러 가기", "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/")
with col4:
    st.link_button("판정 분석 보러 가기", "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video1_sttran")
