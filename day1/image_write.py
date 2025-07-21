import cv2
import numpy as np

# 높이가 400픽셀, 너비가 600픽셀인 흰 배경 이미지를 만든다.
bg = np.ones((400, 600, 3), dtype=np.uint8) * 255

# 직사각형 그리기
# 시작점 => 화면 좌측상단에서 왼쪽으로 100px, 아래로 100px
# 직사각형의 높이와 너비는 각각 50px
# 파란색 (255, 0, 0)
cv2.rectangle(bg, (100, 100), (150, 150), (255, 0, 0), 2)

# 원 그리기
# 중심점 => 화면 좌측상단에서 왼쪽으로 400px, 아래로 100px
# 반지름은 50px
# 초록색 (0, 255, 0)
cv2.circle(bg, (400, 100), 50, (0, 255, 0), -1)

cv2.imshow("결과를 보여주는 창", bg)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("test.jpg", bg)