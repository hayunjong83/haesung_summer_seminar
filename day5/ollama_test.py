# 실습 3 : 실행중인 Ollama에 답변 생성을 요청하기.

import ollama
import time

# 질문하려는 문장
question = "루게릭병에 대해서 알려주세요."
messages = [
  {
    "role": "user",
    "content": question
  }
]

# Ollama 서버에 답변요청 : 참고를 위해 실행시간 측정
start = time.time()    # 시작 시간
response = ollama.chat(
  model = "alibayram/medgemma",
  messages = messages
)
end = time.time()       # 종료 시간

# 답변출력
print(response['message']['content'])
print(f"실행시간 {end - start:.5f} 초")