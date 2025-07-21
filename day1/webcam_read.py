import cv2

cap = cv2.VideoCapture(0)
if cap.isOpened():
  while True:
    ret, img = cap.read()
    if ret:
      cv2.imshow("웹캠을 보여주는 창", img)
    else:
      print("카메라에서 영상을 읽을 수 없습니다.")
      break

    if cv2.waitKey(1) == ord('q'):
      break
else:
  print("웹캠 카메라를 열 수 없습니다.")

cap.release()
cv2.destroyAllWindows()