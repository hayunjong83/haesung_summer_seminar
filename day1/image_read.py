import cv2

# 불러올 이미지의 주소(=경로)를 입력한다.
image_path = "day1_1.jpg"
image = cv2.imread(image_path)

cv2.imshow("이미지를 보여주는 창", image)
cv2.waitKey(0)
cv2.destroyAllWindows()