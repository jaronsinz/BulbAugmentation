import numpy as np
import cv2
import cvzone
import random
import json

#reading json
with open("input/labels/test_json.json", "r") as file_path:
    label_file = json.load(file_path)

#reading all images
img_original = cv2.imread("input/images/background_test.jpg")
img_red_bulb = cv2.imread("bulb_images/red_bulb.png", cv2.IMREAD_UNCHANGED)
#img_red_bulb = cv2.resize(img_red_bulb, down_points, interpolation= cv2.INTER_LINEAR)
img_yellow_bulb = cv2.imread("bulb_images/yellow_bulb.png", cv2.IMREAD_UNCHANGED)
img_green_bulb = cv2.imread("bulb_images/green_bulb.png", cv2.IMREAD_UNCHANGED)

#choosing random bulb to overlay
bulb_list = [img_red_bulb, img_yellow_bulb, img_green_bulb]
random_image = bulb_list[random.randint(0, 2)]

#getting position to overlay from label_file
coordinates = label_file["openlabel"]["frames"]["0"]["objects"]["12345678-1234-1234-1234-123456789123"]["object_data"]["bbox"][0]["val"]

#calculating size of bulb
height_original, width_original, c = img_original.shape

bulb_width = int((width_original*coordinates[2])-(width_original*coordinates[0]))
bulb_height = int((height_original*coordinates[3])-(height_original*coordinates[1]))
new_bulb_dim = (bulb_width, bulb_height)
print(new_bulb_dim)

#resizing image
print(random_image.shape)
resized_image = cv2.resize(random_image, new_bulb_dim)
print(resized_image.shape)

#overlaying image
img_result = cvzone.overlayPNG(img_original, resized_image, [420, 145])

#img_result = cvzone.overlayPNG(img_original, img_red_bulb, [0, 0])

cv2.imshow("Image", img_original)
cv2.imshow("Image", img_result)
cv2.waitKey(0)