# 기본적인 YOLO 모델 사용법
# 필요한 라이브러리를 불러온다.
from ultralytics import YOLO
import cv2

# 사전훈련된 모델은 다음의 하나를 입력할 수 있다.
# (1) yolo11n.pt  (2) yolo11s.pt
# (3) yolo11m.pt  (4) yolo11l.pt  (5) yolo11x.pt
model = YOLO("yolo11s.pt")

# 객체탐지를 실행한다.
image_path = "image1.jpg"
results = model(image_path)

# 실행결과를 저장한다.
results[0].save("result1.jpg")

# 결과 이미지를 화면에 띄워본다.
img = results[0].plot()
cv2.imshow("이미지를 보여주는 창", img)
cv2.waitKey(0)
cv2.destroyAllWindows()