from ultralytics import solutions
import cv2

video_path = "ex2.mp4"
cap = cv2.VideoCapture(video_path)
# 영상정보를 얻는다.
fps = cap.get(cv2.CAP_PROP_FPS)             # 초당 재생속도(fps)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 영상의 가로길이(너비)
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 영상의 세로길이(높이)

counter = solutions.ObjectCounter(
  show=True,
  region=[(430, 150), (550, 150)],     # 관찰할 영역을 지정한다.
  model = "yolo11l.pt",
  # classes = [2],
)

while cap.isOpened():
  ret, img = cap.read()
  if ret:
    results = counter(img)
    # cv2.imshow("video", results.plot_im)

    if cv2.waitKey(30) == ord('q'):
      break
  
  else:
    break

cap.release()
cv2.destroyAllWindows()