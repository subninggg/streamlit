import streamlit as st
import time

col1, col2, col3 = st.columns(3)

with col1:
    st.write('원본 영상')
    st.video('https://file.notion.so/f/f/28b7e521-0e53-4f97-b19b-3c7008fb8ca0/56953f95-95aa-494e-97f2-efc84cdda867/ge_out21.mp4?id=4a5c9c26-71cb-4736-bb35-c0a6f580d2a5&table=block&spaceId=28b7e521-0e53-4f97-b19b-3c7008fb8ca0&expirationTimestamp=1715680800000&signature=rNVjXp7O_MMxt7bQ4akgfvBsFicMAyjqE52rZSF5Blg&downloadName=ge_out21.mp4', format="video/mp4")

with col2:
    st.write('분석 영상')
    st.video('https://youtu.be/Dan-UpqtzL4?si=VfdQ9MRT4e7F2SH9', format="video/mp4")
with col3:
    st.error('OUT')


st.write('분석 과정')
st.image('https://raw.githubusercontent.com/subninggg/streamlit/main/hiera_image/ge_out21_hiera.png')
