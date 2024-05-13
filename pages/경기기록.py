import streamlit as st
import datetime
import pandas as pd

st.title('LSK 2024')
st.header('경기 기록')

option = st.selectbox(
    "요청팀",
    ("전체", "LG 트윈스", "KT 위즈", "SSG 랜더스", "NC 다이노스", "두산 베어스", "KIA 타이거즈", "롯데 자이언츠", "삼성 라이온즈", "한화 이글스", "키움 히어로즈"))

LG = "https://i.namu.wiki/i/Yh75KbIFHGxtCLOMIY9QO3PUpBU6BUPs7dx4_fGuSiWaM6jJ6pfjWDngyEHUQyhoURVdNFAQNM_lXQfhMCoOSNjIpuA-WHULjFjledIqzK0i13S8zEGl9qgPIZFMKtxAP8DyI_sEOAScBzq6IZyknQ.svg"
KT = "https://i.namu.wiki/i/NMhFTHj-iGuzT4J7zWs2WwYBQKGMeei1iNWk6Vv1ifT1xUwMl2z8LSYpaIrZAFPRyGfmXYI9yN5WXt6kUWSe3w.svg"
SSG = "https://i.namu.wiki/i/Ra9t9Odu4mKHO3ejR5jRuHQ0340POkoIb91c8wfoc4hqUbVI9bsqfEpcpGuz4HxR1d4ZgXGnhR6WPrGaMMqVPA6UvpK3Hm7lFpZ7hBIyjhJymUC7k2133SnSijKa8pLrrTMXohDnJkJ3KhqRavEPZw.svg"
NC =  "https://i.namu.wiki/i/3SxNn4aK1kpu4s4fvUYCUV5qRzPl3UqbkfBjChTGQKQzz8Ig3Ek7b0uZU-Vj4N7HMuTvuGO2lPIcr4j5y2ipK2e9RRLXC3zcyqFCbD_MU5ccH6RRL1mYl5WW6uVL6mbfp2O3OUnWQGfISECUFx559g.svg"
두산 = "https://i.namu.wiki/i/BFXATOQ-PRPa5eh2Xh0gEg76MRpufIwtSF8FDT8lykHKUpslrULXZUDZH9XTaup70kLQjacri-uVJdAbBL2AtaLJj9ADIuGcUq1AJQFzbNVULvdgoO-6LazsELU3Y_ioUM08skY7bK-bjxDpnTe-VA.svg"
KIA = "https://i.namu.wiki/i/ZBYDIg8lFfcrlUsHc8IMVjb6sOVrbE53fH4tvqEfvFDX3Juzn8TICz0RVmmlaoefrOt5f-d2lMKH2L80w-tAe1faY6G7epztxfgJ0ffohAZun5-H7V3h1sDw_Y0Cw3Onq3tY2YLKpV6Mwj80C-JU9Q.svg"
롯데 = "https://i.namu.wiki/i/hXIuOi9uZG1lEQmFmrR9MqnXc4D6iE4LRCqE4o3yKRtglYp7epe20FYAWQ8Wo9qFB8Gkdzehh4a0taOCD4H6q1agAIL09IFyQPQ7O3kVa60cNvTIwJ91M4f1c6afctFzeUOrUqAjWa5mlzwer3CHSQ.svg"
삼성 = "https://i.namu.wiki/i/HeuZK6QKFrkNlBq2JhnAx8UkVUAB1MV2Gg9UQ7uq9EspYMHps86lRFpNYIz-xf1y3ouNk5BVRn8lYPUoKNFk-cNkFBRWrvRGyqrZlPHxrnOCP-hcJWzhMRhtIIPBUkqFfCzDhMgRVXi51I3b7QPWnA.svg"
한화 = "https://i.namu.wiki/i/LZYPjPbsbObem4ZvCJDSLoeOd6p3FLIRWLCdcnOK4o7K3_NRha0lhuIpEL4aEjbyYn7uNOR_xAspX2GVI1BFrlr7spl8wiTGanh-HhSzWM9qynLRq_7DeAdsM3MBPqKKYwswMAN11QvscE4-NI6Z2A.svg"
키움 = "https://i.namu.wiki/i/j4a8flSMkAGfrduLvHBnJn7aRSr1STWsyTQ_XpQB-bmflDtaie75yTrISEiso1mBmmvARidtvLkbNZzJhB7TPIO2OB8n20FJKyKlF2U2QDvrUPZQeGJ69KgoJj7zHAEHuyElN7UdIUTFVos6b5e9LQ.svg"

video0 = "https://github.com/subninggg/streamlit/blob/main/capture/ge_out21_crop.png?raw=true"
video1 = "https://github.com/subninggg/streamlit/blob/main/capture/ge_safe2_crop.png?raw=true"
video2 = "https://github.com/subninggg/streamlit/blob/main/capture/ge_safe20_crop.png?raw=true"
video3 = "https://github.com/subninggg/streamlit/blob/main/capture/ge_safe24_crop.png?raw=true"
video4 = "https://github.com/subninggg/streamlit/blob/main/capture/ge_safe28_crop.png?raw=true"
video5 = "https://github.com/subninggg/streamlit/blob/main/capture/jy_out4_crop.png?raw=true"
video6 = "https://github.com/subninggg/streamlit/blob/main/capture/sb_out4_crop.png?raw=true"
video7 = "https://github.com/subninggg/streamlit/blob/main/capture/sb_out5_crop.png?raw=true"
video8 = "https://github.com/subninggg/streamlit/blob/main/capture/sb_out24_crop.png?raw=true"
video9 = "https://github.com/subninggg/streamlit/blob/main/capture/sb_safe15_crop.png?raw=true"

video0_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video0"
video1_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video1"
video2_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video2"
video3_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video3"
video4_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video4"
video5_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video5"
video6_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video6"
video7_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video7"
video8_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video8"
video9_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video9"

if option == "전체":
    df = pd.DataFrame(
        {
            "home": [한화, KIA, KIA, 삼성, KIA, LG, 롯데, 롯데, KT, LG],
            "away": [롯데, KT, LG, KIA, LG, 삼성, LG, LG, 삼성, KIA],
            "call": ["out", "safe", "safe", "safe", "safe", "out", "out", "out", "out", "safe"],
            "video": [video0, video1, video2, video3, video4, video5, video6, video7, video8, video9],
            "link" : [video0_link, video1_link, video2_link, video3_link, video4_link, video5_link, video6_link, video7_link, video8_link, video9_link]
        }
    )
if option == "LG 트윈스":
    df = pd.DataFrame(
        {
            "home": [KIA, KIA, LG, 롯데, 롯데, LG],
            "away": [LG, LG, 삼성, LG, LG, KIA],
            "call": ["safe", "safe", "out", "out", "out", "safe"],
            "video": [video2, video4, video5, video6, video7, video9],
            "link" : [video2_link, video4_link, video5_link, video6_link, video7_link, video9_link]
        }
    )

st.dataframe(
    df,
    column_config={
        "home": st.column_config.ImageColumn(
            "홈"
        ),
        "away": st.column_config.ImageColumn(
            "원정"
        ),
        "call": "판정",
        "video": st.column_config.ImageColumn(
            "영상"
        ),
        "link": st.column_config.LinkColumn(
            "링크",
        )
    },
    hide_index=True,
)
