import cv2
import numpy as np

# 입력 비디오 경로
video1_path = "day1_2.mp4"
video2_path = "test4.mp4"

cap1 = cv2.VideoCapture(video1_path)
cap2 = cv2.VideoCapture(video2_path)

# 영상정보를 얻는다.
fps = cap1.get(cv2.CAP_PROP_FPS)
w = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 저장을 위한 설정
result_path = "test6.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(result_path, fourcc, fps, (w * 2, h))

while cap1.isOpened() and cap2.isOpened():
  ret1, img1 = cap1.read()
  ret2, img2 = cap2.read()

  if not (ret1 and ret2):
      break

  # 가로로 붙이기
  result = np.hstack((img1, img2))

  out.write(result)

  cv2.imshow("Concatenated Video", result)
  if cv2.waitKey(33) & 0xFF == ord('q'):
      break

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()