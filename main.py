import numpy as np
import cv2

img_original = cv2.imread("input/images/background_test.jpg")
img_yellow_bulb = cv2.imread("bulb_images/yellow_bulb.png")

cv2.imshow("Image", img_original)
cv2.waitKey(0)