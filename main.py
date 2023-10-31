import numpy as np
import cv2
import cvzone
import random
import json

#reading label file
with open("input/labels/test_json.json", "r") as file_path:
    label_file = json.load(file_path)

#reading all overlay bulbs
img_red_bulb = cv2.imread("bulb_images/red_bulb.png", cv2.IMREAD_UNCHANGED)
img_yellow_bulb = cv2.imread("bulb_images/yellow_bulb.png", cv2.IMREAD_UNCHANGED)
img_green_bulb = cv2.imread("bulb_images/green_bulb.png", cv2.IMREAD_UNCHANGED)
bulb_list = [img_red_bulb, img_yellow_bulb, img_green_bulb]     #adjust depending on number of bulb images

#loop through all images
for image in label_file["openlabel"]["frames"]:
    #reading current image
    img_original_name = label_file["openlabel"]["frames"][image]["frame_properties"]["streams"]["FC1"]["uri"]
    img_original = cv2.imread(f"input/images/{img_original_name}")

    #getting dimensions of original image
    height_original, width_original, c = img_original.shape
    
    #loop through all inactive bulbs
    for inactive_bulb in label_file["openlabel"]["frames"]["0"]["objects"]:
        #choosing randomly which bulb to overlay
        overlay_bool = random.choice([True, False])                    #add False after loop is done
        if(overlay_bool):
            #choosing random bulb to overlay
            random_overlay_bulb = bulb_list[random.randint(0, 2)]      #adjust depending on number of bulb images
            
            #getting position to overlay from label_file
            coordinates = label_file["openlabel"]["frames"][image]["objects"][inactive_bulb]["object_data"]["bbox"][0]["val"]
            
            #calculating size of bulb
            width_start = int(width_original*coordinates[0])
            height_start = int(height_original*coordinates[1])
            width_end = int(width_original*coordinates[2])
            height_end = int(height_original*coordinates[3])

            bulb_width = width_end-width_start
            bulb_height = height_end-height_start
            new_bulb_dim = (bulb_width, bulb_height)

            #resizing overlay bulb 
            resized_overlay_bulb = cv2.resize(random_overlay_bulb, new_bulb_dim)

            #overlaying image
            img_original = cvzone.overlayPNG(img_original, resized_overlay_bulb, [width_start, height_start])




cv2.imshow("Image", img_original)
cv2.waitKey(0)