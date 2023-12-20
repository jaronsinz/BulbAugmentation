import numpy as np
import cv2
import cvzone
import random
import json
import os

#reading label file
with open("input/labels/test_json.json", "r") as file_path:
    label_file = json.load(file_path)

#reading all overlay bulbs
overlay_bulb_list = []
for overlay_bulb_file in os.listdir("bulb_images"):
    current_overlay_bulb = cv2.imread(f"bulb_images/{overlay_bulb_file}", cv2.IMREAD_UNCHANGED)
    overlay_bulb_list.append(current_overlay_bulb)

#loop through all images
for image in label_file["openlabel"]["frames"]:
    #reading current image
    img_original_name = label_file["openlabel"]["frames"][image]["frame_properties"]["streams"]["FC1"]["uri"][:-4]
    img_original = cv2.imread(f"input/images/{img_original_name}.jpg")

    #set output paths for current image
    label_output_path = f"output/labels/{img_original_name}.txt"
    img_output_path = f"output/images/{img_original_name}.jpg"

    #getting dimensions of original image
    height_original, width_original, c = img_original.shape
    
    #loop through all inactive bulbs
    for inactive_bulb in label_file["openlabel"]["frames"][image]["objects"]:
        #choosing randomly which bulb to overlay
        overlay_bool = random.choice([True, False])                    
        if(overlay_bool):
            #choosing random bulb to overlay
            overlay_bulb_id = random.randint(0, (len(overlay_bulb_list)-1))
            random_overlay_bulb = overlay_bulb_list[overlay_bulb_id]      
            
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

            #create label file for augmented image
            with open(label_output_path, "a") as new_label_file:
                new_label_file.write(f"{overlay_bulb_id} {width_start} {height_start} {width_end} {height_end}\n")

        cv2.imwrite(img_output_path, img_original)