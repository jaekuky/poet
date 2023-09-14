# env 파일을 사용하기 위한 라이브러리 import
# from dotenv import load_dotenv
# load_dotenv()

# langchain, chat 모드 사용   
from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

# Llama 사용
# from langchain.llms import CTransformers
# lim = CTransformers(
#     model ="llama-2-7b-chat.ggmlv3.q6_K.bin",
#     model_type = "llama"
# )

# streamlit으로 Frontend 만들기
import streamlit as st
from PIL import Image

# 화면 상단 여백 제거
st.write("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

# 웹페이지 제목
st.title("AI & Poem")
st.markdown("### Your Topics, Our AI Poems")

# 그림 삽입
pictureCols = []
pictureCols = st.columns([0.25, 0.5, 0.25])
with pictureCols[1]:
    img = Image.open("AI-Poet.png")
    st.image(img)

# 시 주제 입력 받음
content = st.text_input("시의 주제를 제시해 주세요")
    
# 버튼 만들기
# 시 작성 & 시 낭송
from gtts import gTTS
if st.button("시 작성 요청"):
    with st.spinner("시 작성 중... 잠시만 기다려 주세요"):
        # 시 작성
        poem  = chat_model.predict(content + "에 대한 시를 써주세요")
        st.write(poem)

    with st.spinner("시 낭송을 위한 음성 준비중... 잠시만 기다려 주세요"):
        # Google TTS를 사용하여 시 낭송
        tts = gTTS(text=poem, lang="ko", slow=False)
        tts.save("poem.mp3")
        st.audio("poem.mp3")
   
# 수익화
from streamlit_extras.buy_me_a_coffee import button
button(username="jakukyr", floating=True, font="Lato", width=221) 

st.write("Powered by ChatGPT and LangChain")
