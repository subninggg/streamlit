import streamlit as st

LG = "https://i.namu.wiki/i/Yh75KbIFHGxtCLOMIY9QO3PUpBU6BUPs7dx4_fGuSiWaM6jJ6pfjWDngyEHUQyhoURVdNFAQNM_lXQfhMCoOSNjIpuA-WHULjFjledIqzK0i13S8zEGl9qgPIZFMKtxAP8DyI_sEOAScBzq6IZyknQ.svg"
KT = "https://content.sportslogos.net/logos/84/6733/full/4695__kt_wiz-primary-2015.png"
SSG = "https://i.namu.wiki/i/Ra9t9Odu4mKHO3ejR5jRuHQ0340POkoIb91c8wfoc4hqUbVI9bsqfEpcpGuz4HxR1d4ZgXGnhR6WPrGaMMqVPA6UvpK3Hm7lFpZ7hBIyjhJymUC7k2133SnSijKa8pLrrTMXohDnJkJ3KhqRavEPZw.svg"
NC =  "https://i.namu.wiki/i/3SxNn4aK1kpu4s4fvUYCUV5qRzPl3UqbkfBjChTGQKQzz8Ig3Ek7b0uZU-Vj4N7HMuTvuGO2lPIcr4j5y2ipK2e9RRLXC3zcyqFCbD_MU5ccH6RRL1mYl5WW6uVL6mbfp2O3OUnWQGfISECUFx559g.svg"
두산 = "https://i.namu.wiki/i/BFXATOQ-PRPa5eh2Xh0gEg76MRpufIwtSF8FDT8lykHKUpslrULXZUDZH9XTaup70kLQjacri-uVJdAbBL2AtaLJj9ADIuGcUq1AJQFzbNVULvdgoO-6LazsELU3Y_ioUM08skY7bK-bjxDpnTe-VA.svg"
KIA = "https://i.namu.wiki/i/ZBYDIg8lFfcrlUsHc8IMVjb6sOVrbE53fH4tvqEfvFDX3Juzn8TICz0RVmmlaoefrOt5f-d2lMKH2L80w-tAe1faY6G7epztxfgJ0ffohAZun5-H7V3h1sDw_Y0Cw3Onq3tY2YLKpV6Mwj80C-JU9Q.svg"
롯데 = "https://i.namu.wiki/i/hXIuOi9uZG1lEQmFmrR9MqnXc4D6iE4LRCqE4o3yKRtglYp7epe20FYAWQ8Wo9qFB8Gkdzehh4a0taOCD4H6q1agAIL09IFyQPQ7O3kVa60cNvTIwJ91M4f1c6afctFzeUOrUqAjWa5mlzwer3CHSQ.svg"
삼성 = "https://i.namu.wiki/i/HeuZK6QKFrkNlBq2JhnAx8UkVUAB1MV2Gg9UQ7uq9EspYMHps86lRFpNYIz-xf1y3ouNk5BVRn8lYPUoKNFk-cNkFBRWrvRGyqrZlPHxrnOCP-hcJWzhMRhtIIPBUkqFfCzDhMgRVXi51I3b7QPWnA.svg"
한화 = "https://i.namu.wiki/i/LZYPjPbsbObem4ZvCJDSLoeOd6p3FLIRWLCdcnOK4o7K3_NRha0lhuIpEL4aEjbyYn7uNOR_xAspX2GVI1BFrlr7spl8wiTGanh-HhSzWM9qynLRq_7DeAdsM3MBPqKKYwswMAN11QvscE4-NI6Z2A.svg"
키움 = "https://i.namu.wiki/i/j4a8flSMkAGfrduLvHBnJn7aRSr1STWsyTQ_XpQB-bmflDtaie75yTrISEiso1mBmmvARidtvLkbNZzJhB7TPIO2OB8n20FJKyKlF2U2QDvrUPZQeGJ69KgoJj7zHAEHuyElN7UdIUTFVos6b5e9LQ.svg"

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.image(롯데)
with col2:
    st.image('https://st4.depositphotos.com/1404656/30086/v/450/depositphotos_300867228-stock-illustration-versus-sign-black-and-white.jpg')
with col3:
    st.image(LG)


st.subheader('분석 영상')
st.image('https://github.com/subninggg/streamlit/blob/main/sttran_gif/sb_out4_sttran.gif?raw=true')
st.page_link("pages/video6.py", label="태그 영상")
