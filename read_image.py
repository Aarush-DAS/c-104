import cv2

img=cv2.imread('butterfly.jpg')
cv2.imshow("display_image",img)
#print(img)

gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Grayscale", gray_img)

cv2.waitKey(0)



