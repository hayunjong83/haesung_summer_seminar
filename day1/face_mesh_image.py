import cv2
import mediapipe as mp
import numpy as np
import math

# 직접 설정해야 하는 부분 (1) 이미지 경로, (2) 저장할 파일명
image_path = "day1_4.jpg"
result_path = "test7.jpg"

# 두 점 사이의 기울어진 각도를 구하는 함수
def get_angle(p1, p2):
  dx = p2[0] - p1[0]
  dy = p2[1] - p1[1]
  return math.degrees(math.atan2(dy, dx))

# 각도에 맞춰서 이미지를 회전시키는 함수
def rotate_image(image, angle):
  h, w, _ = image.shape
  center = (w//2, h//2)
  rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
  rotated = cv2.warpAffine(image, rot_mat, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_TRANSPARENT)
  return rotated

# 이미지에서 랜드마크를 찾고, 결과 이미지를 저장한다.
def find_and_draw(image_path, result_path):
  img = cv2.imread(image_path)
  h, w, c = img.shape

  # 선글라스 이미지를 투명하게 읽어오기
  sunglasses = cv2.imread("black_sunglass.png", cv2.IMREAD_UNCHANGED)
  glass_h, glass_w, glass_c = sunglasses.shape

  # 미디어파이프 랜드마크모델 
  mp_face_mesh = mp.solutions.face_mesh
  face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False,
                                    max_num_faces=1,
                                    refine_landmarks=True,
                                    min_detection_confidence=0.5,
                                    min_tracking_confidence=0.5)

  # 원본이미지를 RGB 모드로 변경
  src = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  # 랜드마크 탐색
  results = face_mesh.process(src)

  # 필요한 인덱스 검색 : 
  # https://storage.googleapis.com/mediapipe-assets/documentation/mediapipe_face_landmark_fullsize.png
  LEFT_EYE_INDEX = 33
  RIGHT_EYE_INDEX = 263

  if results.multi_face_landmarks:
    for landmark in results.multi_face_landmarks:
      lmks = landmark.landmark
      
      # 왼쪽눈 끝(x1, y1)과 오른쪽 눈(x2, y2) 좌표 계산
      x1 = int(lmks[LEFT_EYE_INDEX].x * w)
      y1 = int(lmks[LEFT_EYE_INDEX].y * h)
      x2 = int(lmks[RIGHT_EYE_INDEX].x * w)
      y2 = int(lmks[RIGHT_EYE_INDEX].y * h)

      # 눈의 중심 좌표와 두 눈 사이의 기울어진 각도 계산
      angle = get_angle((x1, y1), (x2, y2))
      center_x = (x1 + x2) // 2
      center_y = (y1 + y2) // 2 + 20    # 선글라스 크기때문에 임의로 조정

      # 변경할 선글라스 크기 결정
      sunglass_width = int(1.5 * abs(x2 - x1))
      sunglass_height = int(sunglass_width * glass_h / glass_w)
      
      # 선글라스 리사이즈
      resized_sunglasses = cv2.resize(sunglasses, (sunglass_width, sunglass_height))
      rotated_sunglasses = rotate_image(resized_sunglasses, -angle)
      rh, rw = rotated_sunglasses.shape[:2]

      # 선글라스 합성할 위치
      top_left_x = center_x - rw // 2
      top_left_y = center_y - rh // 2

      # 합성
      for i in range(rh):
        for j in range(rw):
          y = top_left_y + i
          x = top_left_x + j

          if 0 <= x < w and 0 <= y < h:
            alpha = rotated_sunglasses[i, j, 3] / 255.0  # 투명도
            if alpha > 0:
              for c in range(3):
                img[y, x, c] = (1 - alpha) * img[y, x, c] + alpha * rotated_sunglasses[i, j, c]

  # 결과 출력
  cv2.imshow("선글라스 합성 결과", img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

  cv2.imwrite(result_path, img)

# 위에서 선언한 함수를 이용해서, 실제 결과를 내는 부분
find_and_draw(image_path, result_path)