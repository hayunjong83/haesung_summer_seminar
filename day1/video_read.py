import cv2

# 불러올 동영상의 주소(=경로)를 입력한다.
video_path = "day1_2.mp4"

cap = cv2.VideoCapture(video_path)
if cap.isOpened():
  while True:
    ret, img = cap.read()
    if ret:
      cv2.imshow("영상을 보여주는 창", img)
    else:
      break

    if cv2.waitKey(30) == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()