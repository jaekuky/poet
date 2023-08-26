# env 파일을 사용하기 위한 라이브러리 import
from dotenv import load_dotenv
load_dotenv()

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
st.title('인공지능 시인')
content = st.text_input('시의 주제를 제시해 주세요')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):
        result  = chat_model.predict("Write poem about" + content)
        st.write(result)
