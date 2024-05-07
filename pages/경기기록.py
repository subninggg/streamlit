import streamlit as st
import datetime

st.title('LSK 2024')
st.header('경기 기록')

option = st.selectbox(
    "요청팀",
    ("LG 트윈스", "KT 위즈", "SSG 랜더스", "NC 다이노스", "두산 베어스", "KIA 타이거즈", "롯데 자이언츠", "삼성 라이온즈", "한화 이글스", "키움 히어로즈"))

d = st.date_input("경기일자", datetime.date(2019, 7, 6))