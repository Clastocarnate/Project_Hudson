import cv2

img = cv2.imread("IMG_2650.jpeg")
img = cv2.resize(img, (1450,1300))
cv2.imshow("Me", img)
cv2.waitKey(0)
cv2.destroyAllWindows()