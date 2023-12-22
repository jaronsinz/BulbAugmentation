import json
import os
import uuid

#count number of labeled files
label_files_path = "/input/labels/txt"
number_of_labeled_files = 0
for path in os.listdir(label_files_path):
    number_of_labeled_files += 1

#values that need to be hardcoded
frame_intervals = [
                    {
                        "frame_end": number_of_labeled_files - 1,
                        "frame_start": 0
                     }
                ]

frame_contexts = {
                    "0": {
                        "context_data": {
                            "vec": [
                                {
                                    "name": "value",
                                    "val": [
                                        "Clear/Sunny"
                                    ]
                                }
                            ]
                        }
                    },
                    "1": {
                        "context_data": {
                            "vec": [
                                {
                                    "name": "value",
                                    "val": [
                                        "Snow"
                                    ]
                                }
                            ]
                        }
                    },
                    "2": {
                        "context_data": {
                            "vec": [
                                {
                                    "name": "value",
                                    "val": [
                                        "City"
                                    ]
                                }
                            ]
                        }
                    },
                    "3": {
                        "context_data": {
                            "vec": [
                                {
                                    "name": "value",
                                    "val": [
                                        "DE"
                                    ]
                                }
                            ]
                        }
                    }
                }

metadata = {
            "annotation_id": 4799264,
            "annotation_instruction": "2023-03-24-001",
            "annotation_type": "2DBbox",
            "batch": "TaskID_2",
            "input_external_id": "185",
            "input_uuid": "0b2bf7d3-ebd0-409d-a4ca-d0eb399d962a",
            "project": "pace_alliance_tld",
            "schema_version": "1.0.0",
            "uri": "app.kognic.com/view/assignment/f85416ad-6a4f-4264-a9fa-24340d5e8b32",
            "uuid": "1ed33f69-7f1c-47b3-af68-2d82a516a96a",
            "label_spec_version": "6.0.0"
        }

streams = {
            "FC1": {
                "description": "",
                "stream_properties": {
                    "height": 3074,                         #change?
                    "width": 6090
                },
                "type": "camera"
            }
        }

def get_frame_properties(frame_id:int, label_file:str):
    img_file_name = label_file[9:-3] + "png"
    frame_properties = {
        "external_id": frame_id,
                    "streams": {
                        "FC1": {
                            "uri": img_file_name
                        }
                    },
                    "timestamp": 100
    }
    return frame_properties

def centralize_bounding_box(x,y,w,h):
    x1, y1 = x-w/2, y-h/2
    x2, y2 = x+w/2, y+h/2
    print(str(x1) + ", " + str(y1) + ", " + str(x2) + ", " + str(y2))
    return x1, y1, x2, y2

def get_bbox(bbox_list_centralized):
    object_short_uuid= str(uuid.uuid4())[:8]
    bbox = [
                                {
                                    "attributes": {
                                        "boolean": [
                                            {
                                                "name": "interpolated",
                                                "val": False
                                            }
                                        ],
                                        "text": [
                                            {
                                                "name": "stream",
                                                "val": "FC1"
                                            }
                                        ]
                                    },
                                    "name": f"bbox-{object_short_uuid}",
                                    "val": [
                                        float(bbox_list_centralized[0]),            #values need to be converted
                                        float(bbox_list_centralized[1]),            
                                        float(bbox_list_centralized[2]),
                                        float(bbox_list_centralized[3])
                                    ]
                                }
                            ]
    return bbox

def get_boolean():
    boolean = [
                                {
                                    "name": "isDecipherable",
                                    "val": True
                                },
                                {
                                    "name": "isBoundingBoxEstimated",
                                    "val": False
                                },
                                {
                                    "name": "isWarningOnly",
                                    "val": False
                                }
            ]
    return boolean

def get_text():
    text = [
                                {
                                    "name": "occlusion",
                                    "val": "NotOccluded"
                                },
                                {
                                    "name": "truncation",
                                    "val": "NotTruncated"
                                },
                                {
                                    "name": "bulbCount",
                                    "val": "Unsure"
                                },
                                {
                                    "name": "stacking",
                                    "val": "Other"
                                },
                                {
                                    "name": "status",
                                    "val": "Unsure"
                                },
                                {
                                    "name": "relevanceDrivenPath",
                                    "val": "NotRelevant"
                                },
                                {
                                    "name": "direction",
                                    "val": "Back"
                                },
                                {
                                    "name": "targetRoadUser",
                                    "val": "Unsure"
                                }
            ]
    return text

def get_object(frame_id:int, object_uuid:str):
    object = {
                "frame_intervals": [
                    {
                        "frame_end": frame_id,
                        "frame_start": frame_id
                    }
                ],
                "name": object_uuid,
                "object_data": {},
                "type": "TrafficLightBulbInactive"
            }
    return object

#--------------------generating first hardcoded dicts--------------------------
inactive_bulb_olf = {}
inactive_bulb_olf["openlabel"] = {}
inactive_bulb_olf["openlabel"]["actions"] = {}
inactive_bulb_olf["openlabel"]["contexts"] = {
            "0": {
                "name": "",
                "type": "WeatherSky"
            },
            "1": {
                "name": "",
                "type": "WeatherPrecipitation"
            },
            "2": {
                "name": "",
                "type": "RoadTypes"
            },
            "3": {
                "name": "",
                "type": "Country"
            }
        }
inactive_bulb_olf["openlabel"]["coordinate_systems"] = {}
inactive_bulb_olf["openlabel"]["events"] = {}
inactive_bulb_olf["openlabel"]["frame_intervals"] = frame_intervals

#--------------------generating frames dict-------------------------------------

inactive_bulb_olf["openlabel"]["frames"] = {}

#create new frame for every labeled image
frame_id = 0
objects = {}
for label_file in os.listdir("/input/labels/txt"):
    inactive_bulb_olf["openlabel"]["frames"][frame_id] = {}
    inactive_bulb_olf["openlabel"]["frames"][frame_id]["contexts"] = frame_contexts
    inactive_bulb_olf["openlabel"]["frames"][frame_id]["frame_properties"] = get_frame_properties(frame_id, label_file)

    #create new objects dict for every frame containing all labeled inactive bulbs in the current frame with their uuid and bbox-coordinates
    frames_objects = {}
    with open(f"/input/labels/txt/{label_file}") as current_label_file:
        for line in current_label_file:
            object_uuid = str(uuid.uuid4())
            bbox_list = line[2:].split()
            bbox_list_centralized = centralize_bounding_box(float(bbox_list[0]), float(bbox_list[1]), float(bbox_list[2]), float(bbox_list[3]))
            #create list of all objects in relation to a frame
            frames_objects[object_uuid] = {}
            frames_objects[object_uuid]["object_data"] = {}
            frames_objects[object_uuid]["object_data"]["bbox"] = get_bbox(bbox_list_centralized) 
            frames_objects[object_uuid]["object_data"]["boolean"] = get_boolean()
            frames_objects[object_uuid]["object_data"]["text"] = get_text()

            #create list of all objects
            objects[object_uuid] = get_object(frame_id, object_uuid)

    inactive_bulb_olf["openlabel"]["frames"][frame_id]["objects"] = frames_objects
    inactive_bulb_olf["openlabel"]["frames"][frame_id]["relations"] = {}
    inactive_bulb_olf["openlabel"]["metadata"] = metadata
    inactive_bulb_olf["openlabel"]["objects"] = objects
    inactive_bulb_olf["openlabel"]["ontologies"] = {}
    inactive_bulb_olf["openlabel"]["relations"] = {}                                    #leave out completely?
    inactive_bulb_olf["openlabel"]["resources"] = {}
    inactive_bulb_olf["openlabel"]["streams"] = streams
    inactive_bulb_olf["openlabel"]["tags"] = {}

    frame_id += 1


#saving new OLF file
with open('/input/labels/olf/inactiveBulbsOLF.json', 'w') as json_file:
    json.dump(inactive_bulb_olf, json_file)