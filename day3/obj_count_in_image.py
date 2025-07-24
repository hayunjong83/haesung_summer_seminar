import ultralytics
from ultralytics import solutions
import cv2

# 분석할 비디오 영상 경로를 입력한다.
video_path = "cctv2.mp4"

# 영상을 불러오고, 필요한 정보를 파악한다.
cap = cv2.VideoCapture(video_path)
# 영상정보를 얻는다.
fps = cap.get(cv2.CAP_PROP_FPS)             # 초당 재생속도(fps)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 영상의 가로길이(너비)
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 영상의 세로길이(높이)

region_points = {
  "region-01" : [(20, 20), (300, 20),  (300, 300), (20, 300)],
  "region-02" : [(50, 50), (100, 50),  (100, 100), (100, 50)],
}

# 이미지 내의 객체를 셀 수 있도록 선언한다.
counter = solutions.RegionCounter(
  show=True,
  region=region_points,
  model = "yolo11n.pt"
)


# 영상을 화면에 띄우는 코드
while cap.isOpened():
  ret, img = cap.read()
  if ret:
    results = counter(img)
    cv2.imshow("video", results.plot_im)

    if cv2.waitKey(30) == ord('q'):
      break
  
  else:
    break

cap.release()
cv2.destroyAllWindows()