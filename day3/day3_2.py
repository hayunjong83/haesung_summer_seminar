# 필요한 라이브러리를 불러온다.
from ultralytics import solutions
import cv2

counter = solutions.ObjectCounter(
  show=True,
  model="yolo11s.pt",
)

# 분석할 비디오 영상 경로를 입력한다.
video_path = "cctv1.mp4"
# 영상을 불러온다.
cap = cv2.VideoCapture(video_path)

# 각 프레임마다 객체 개수를 세는 부분
while cap.isOpened():
  ret, img = cap.read()
  if ret:
    results = counter(img)

    if cv2.waitKey(30) == ord('q'):
      break
  else:
    break

cap.release()
cv2.destroyAllWindows()