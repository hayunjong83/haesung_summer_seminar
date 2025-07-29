# 기본적인 YOLO 모델 사용법
# 필요한 라이브러리를 불러온다.
from ultralytics import YOLO
from ultralytics import solutions
import cv2

model = YOLO("yolo11s.pt")
counter = solutions.ObjectCounter(
  show=True,
  model="yolo11s.pt",
  classes = [0]
)

# 객체탐지를 실행한다.
image_path = "image1.jpg"
img = cv2.imread(image_path)
# results = model(image_path)
results = counter(img)

# 실행결과를 저장한다.
# results.save("result2.jpg")
cv2.imwrite("results2.jpg", results.plot_im)
print(f"탐색된 객체의 수 {results}")

# 결과 이미지를 화면에 띄워본다.
# img = results.plot()
cv2.imshow("이미지를 보여주는 창", results.plot_im)
cv2.waitKey(0)
cv2.destroyAllWindows()