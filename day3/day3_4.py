# 기본적인 YOLO 모델 사용법
# 필요한 라이브러리를 불러온다.
from ultralytics import solutions
import cv2

counter = solutions.ObjectBlurrer(
  show=True,
  model="yolo11s.pt",
  classes = [3]
)

# 객체탐지를 실행한다.
image_path = "image1.jpg"
img = cv2.imread(image_path)
results = counter(img)

# 실행결과를 저장한다.
cv2.imwrite("results3.jpg", results.plot_im)
