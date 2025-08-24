# 실습 4 : ollama를 활용하는 챗봇
import streamlit as st
import ollama
import os
import time

# 페이지 제목
st.title("실습 4: Ollama활용 챗봇")

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
  
  # Ollama에 요청할 메시지를 만든다.
  msg = [
    {
      "role": "system",
      "content" : "You are an experienced doctor."
    },
    {
      "role": "user",
      "content": prompt
    }
  ]

  # ollama 서버에 요청하여 답변을 생성한다.
  response = ollama.chat(
    model = "alibayram/medgemma",
    messages = msg
    )
  
  bot_response = response['message']['content']
  with st.chat_message("assistant"):
    st.markdown(bot_response)
  
  # 새로 구성한 챗봇의 대답을 대화내용에 추가한다.
  st.session_state.messages.append(
    {"role": "assistant", "content":bot_response})
