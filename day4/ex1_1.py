from ultralytics import solutions
import cv2

# 주어진 경로의 이미지를 읽는다.
image_path = "ex1.jpg"
img = cv2.imread(image_path)

# 이미지 안에서 자동차(2번 클래스)의 개수만 표현한다.
counter = solutions.ObjectCounter(
  show=False,        # OpenCV로 직접 화면에 띄우기 위해 False
  model="yolo11s.pt",
  classes = [2],
  show_conf = False,
  show_labels = False
)

# 자동자의 개수를 센다.
results = counter(img)

# 결과이미지에서 사람(0번 클래스)은 블러 처리한다.
blurrer = solutions.ObjectBlurrer(
  show =False,        # OpenCV로 직접 화면에 띄우기 위해 False
  model="yolo11s.pt",
  classes = [0],
  show_conf = False,
  show_labels = False,
  verbose = False
)

# 이번에서는 자동차 개수를 센 결과이미지를 입력한다.
results2 = blurrer(results.plot_im)

# 결과 이미지(results.plot_im)를 화면에 띄운다.
cv2.imshow("results", results2.plot_im)

cv2.waitKey(0)    # 바로 사라지지 않게 대기한다.
cv2.destroyAllWindows()