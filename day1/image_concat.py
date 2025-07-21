import cv2
import numpy as np

# 원본 이미지
original = cv2.imread('day1_4.jpg')
# 처리된 이미지
processed = cv2.imread('test2.jpg')

# 가로로 이미지를 연결
result = np.hstack((original, processed))

cv2.imshow("가로로 연결된 이미지", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지 저장
cv2.imwrite("test5.jpg", result)