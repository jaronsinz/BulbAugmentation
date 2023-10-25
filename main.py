import numpy as np
import cv2
import cvzone
import random


#reading all images
img_original = cv2.imread("input/images/background_test.jpg")
img_red_bulb = cv2.imread("bulb_images/red_bulb.png", cv2.IMREAD_UNCHANGED)
#img_red_bulb = cv2.resize(img_red_bulb, down_points, interpolation= cv2.INTER_LINEAR)
img_yellow_bulb = cv2.imread("bulb_images/yellow_bulb.png", cv2.IMREAD_UNCHANGED)
img_green_bulb = cv2.imread("bulb_images/green_bulb.png", cv2.IMREAD_UNCHANGED)

#choosing random bulb to overlay
bulb_list = [img_red_bulb, img_yellow_bulb, img_green_bulb]
random_number = random.randint(0, 2)

#overlaying image
img_result = cvzone.overlayPNG(img_original, bulb_list[random_number], [0, 0])
#down_points = (2000, 2000)

#img_result = cvzone.overlayPNG(img_original, img_red_bulb, [0, 0])

cv2.imshow("Image", img_original)
cv2.imshow("Image", img_result)
cv2.waitKey(0)