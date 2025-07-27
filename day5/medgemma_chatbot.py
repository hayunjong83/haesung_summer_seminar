# 실습 2 : MedGemma가 답변하는 챗봇
import streamlit as st
from transformers import pipeline
import torch
import os

# MedGemma 사용을 위한 허깅페이스 액세스 토큰
HF_TOKEN = "직접발급받은 액세스토큰 값"
os.environ["HF_TOKEN"] = HF_TOKEN

# 페이지 제목
st.title("실습 2: MedGemma 챗봇")

# 진행된 대화내용을 저장하도록 session_state 활용
# 아직 저장된 내용이 없다면, 초기화
if "messages" not in st.session_state:
  st.session_state["messages"] = []

# 저장된 내용이 있다면, 새로운 대화를 추가전에 화면 출력
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# 새로운 사용자 입력을 처리한다.
if prompt := st.chat_input("무엇이든 물어보세요"):
  with st.chat_message("user"):
    st.markdown(prompt)
  
  # 새로 들어온 입력을 기존 대화내용에 추가한다.
  st.session_state.messages.append(
    {"role": "user", "content": prompt})
  
  # 챗봇은 MedGemma를 이용해서 답변을 생성한다.
  pipe = pipeline(
    "image-text-to-text",
    model = "google/medgemma-4b-it",
    torch_dtype = torch.bfloat16,
    device="cpu"
    )
  msg = [
    {
      "role": "system",
      "content" : [{"type": "text", "text": "You are an experienced doctor."}]
    },
    {
      "role": "user",
      "content": [{"type": "text", "text": prompt}]
    }
  ]
  output = pipe(text=msg, max_new_tokens=200)

  bot_response = output[0]["generated_text"][-1]["content"]
  with st.chat_message("assistant"):
    st.markdown(bot_response)

  # 새로 구성한 챗봇의 대답을 대화내용에 추가한다.
  st.session_state.messages.append(
    {"role": "assistant", "content":bot_response})