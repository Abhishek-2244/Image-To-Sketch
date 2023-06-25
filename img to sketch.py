import cv2
img = cv2.imread("Tanjiro.jpg")
img = cv2.resize(img, (400,400))
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_gray_image = 255-gray_image
blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21), 0)
inverted_blurreed_img  = 255 - blurred_img
pencil_sketch_img = cv2.divide(gray_image, inverted_blurreed_img, scale = 255.0)
cv2.imshow("Orignal image", img)
cv2.imshow("Pencile Sketch", pencil_sketch_img)
cv2.waitKey(0)