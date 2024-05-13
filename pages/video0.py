import streamlit as st
import time

col1, col2, col3 = st.columns(3)

with col1:
    st.write('원본 영상')
    st.video('https://file.notion.so/f/f/45a0d939-bfed-4119-9076-4dd32da0565c/f2e78a16-eac0-497d-9287-0f4b604dc89d/ge_out21.mp4?id=6afd496c-e3ef-4d03-9877-1229ff15bd84&table=block&spaceId=45a0d939-bfed-4119-9076-4dd32da0565c&expirationTimestamp=1715731200000&signature=B9Qwc8WTl4aSaddTvnW6_18lIv_RUmN_9zhum9BmOnA&downloadName=ge_out21.mp4', format="video/mp4")

with col2:
    st.write('분석 영상')
    st.video('https://youtu.be/Dan-UpqtzL4?si=VfdQ9MRT4e7F2SH9', format="video/mp4")
with col3:
    st.error('OUT')


st.write('분석 과정')
st.image('https://raw.githubusercontent.com/subninggg/streamlit/main/hiera_image/ge_out21_hiera.png')
