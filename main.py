# langchain, chat 모드 사용   
from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

# streamlit으로 Frontend 만들기
import streamlit as st

# 화면 상단 여백 제거
st.write("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

# 시 주제 입력 받음
st.markdown("#### 주제를 제시해 주시면, 주제에 대한 시를 작성해 드립니다.")
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
