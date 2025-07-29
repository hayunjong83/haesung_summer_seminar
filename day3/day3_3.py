# 필요한 라이브러리를 불러온다.
from ultralytics import solutions
import cv2

counter = solutions.RegionCounter(
  show=True,
  model="yolo11l.pt",
  classes = [0],
  # 단일 영역 설정시
  # region = [(210, 150), (300, 150), (300, 220), (210, 220)],
  # 다중 영역 설정시
  region= {
    "region-01": [(210, 150), (300, 150), (300, 220), (210, 220)],
    "region-02": [(350, 180), (430, 180), (430, 230), (350, 230)],
  },
  show_conf = False,
  show_labels = False
)

# 분석할 비디오 영상 경로를 입력한다.
video_path = "cctv1.mp4"
# 영상을 불러온다.
cap = cv2.VideoCapture(video_path)
# 영상정보를 얻는다.
fps = cap.get(cv2.CAP_PROP_FPS)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 분석된 영상을 저장하기 위한 설정
result_path = "cctv1_result2.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(result_path, fourcc, fps, (w, h))

# 각 프레임마다 객체 개수를 세는 부분
while cap.isOpened():
  ret, img = cap.read()
  if ret:
    results = counter(img)
    out.write(results.plot_im)

    if cv2.waitKey(30) == ord('q'):
      break
  else:
    break

cap.release()
out.release()
cv2.destroyAllWindows()