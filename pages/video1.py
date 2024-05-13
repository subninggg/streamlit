import streamlit as st
import time

col1, col2, col3 = st.columns(3)

with col1:
    st.write('원본 영상')
    st.video('https://file.notion.so/f/f/28b7e521-0e53-4f97-b19b-3c7008fb8ca0/3f81b632-d650-497e-a920-815c6369a2de/ge_safe2.mp4?id=f40ae133-b4fb-4ad5-88a3-14c673dffd0c&table=block&spaceId=28b7e521-0e53-4f97-b19b-3c7008fb8ca0&expirationTimestamp=1715688000000&signature=N3g8qZnk3FXJL6GO5QX4cOnW8FRRaFBrn6rE-ny9yrs&downloadName=ge_safe2.mp4', format="video/mp4")

with col2:
    st.write('분석 영상')
    st.video('https://youtu.be/Dan-UpqtzL4?si=VfdQ9MRT4e7F2SH9', format="video/mp4")
with col3:
    st.error('OUT')
    st.page_link("pages/video0_sttran.py", label="video0_sttran")

st.write('분석 과정')
st.image('https://raw.githubusercontent.com/subninggg/streamlit/main/hiera_image/ge_safe2_hiera.png')
