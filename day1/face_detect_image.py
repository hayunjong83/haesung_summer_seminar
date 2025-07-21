import cv2
import mediapipe as mp

# 이미지를 읽기 & 높이/너비 알아내기
img_path = "day1_5.jpg"
img = cv2.imread(img_path)
h, w, c = img.shape

# 미디어파이프
mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection(
  model_selection = 0,
  min_detection_confidence = 0.5)

# 이미지를 RGB 순서로 바꿔서 입력
src = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 얼굴 탐색 하기
results = face_detection.process(src)

# 탐색한 얼굴 표현하기
if results.detections:
  for det in results.detections:
    bbox = det.location_data.relative_bounding_box
    x = int(bbox.xmin * w)
    y = int(bbox.ymin * h)
    bbox_w = int(bbox.width * w)
    bbox_h = int(bbox.height * h)

    cv2.rectangle(img, 
                  (x, y), (x + bbox_w, y + bbox_h),
                  (0, 255, 0), 2)

# 결과 보여주기
cv2.imshow("얼굴 인식 결과", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 결과 저장
cv2.imwrite("test3.jpg", img)