import cv2
import mediapipe as mp

video_path = "day1_2.mp4"
result_path = "test4.mp4"

# 미디어파이프
mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection(
  model_selection = 1,
  min_detection_confidence = 0.2)

cap = cv2.VideoCapture(video_path)

# 영상정보를 얻는다.
fps = cap.get(cv2.CAP_PROP_FPS)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 저장을 위한 설정
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(result_path, fourcc, fps, (w, h))

while cap.isOpened():
  ret, img = cap.read()

  if ret:
    src = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # 얼굴 탐지
    results = face_detection.process(src)
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
    
    # 영상을 기록
    out.write(img)
    cv2.imshow("얼굴인식결과", img)
    if cv2.waitKey(30) == ord('q'):
      break
  else:
    break

cap.release()
out.release()
cv2.destroyAllWindows()
