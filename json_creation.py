import json

output_path = "input/labels/test_json.json"

test_json = {}
test_json["openlabel"] = {}
test_json["openlabel"]["actions"] = {}
test_json["openlabel"]["contexts"] = {
    "0": {
        "name": "",
        "type": "WeatherSky"
    },
    "1": {
        "name": "",
        "type": "WeatherPrecipitation"
    }
}
test_json["openlabel"]["coordinate_systems"] = {}
test_json["openlabel"]["frames"] = {}
test_json["openlabel"]["frames"]["0"] = {}
test_json["openlabel"]["frames"]["0"]["contexts"] = {}
test_json["openlabel"]["frames"]["0"]["frame_properties"] = {
    "external_id": 0,
    "streams": {
        "FC1": {
            "uri": "background_test.jpg"
        }
    },
    "timestamp": 100
}
test_json["openlabel"]["frames"]["0"]["objects"] = {}
test_json["openlabel"]["frames"]["0"]["objects"]["12345678-1234-1234-1234-123456789123"] = {}
test_json["openlabel"]["frames"]["0"]["objects"]["12345678-1234-1234-1234-123456789123"]["object_data"] = {
    "bbox": [
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
            "name": "bbox-12345678",
            "val": [
                0.42,
                0.134,
                0.58,
                0.28
            ]
        }
    ],
    "boolean": [],
    "text": []
}
test_json["openlabel"]["frames"]["0"]["objects"]["12345678-1234-1234-1234-123456789124"] = {}
test_json["openlabel"]["frames"]["0"]["objects"]["12345678-1234-1234-1234-123456789124"]["object_data"] = {
    "bbox": [
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
            "name": "bbox-12345679",
            "val": [
                0.42,
                0.307,
                0.58,
                0.453
            ]
        }
    ],
    "boolean": [],
    "text": []
}
test_json["openlabel"]["frames"]["0"]["objects"]["12345678-1234-1234-1234-123456789125"] = {}
test_json["openlabel"]["frames"]["0"]["objects"]["12345678-1234-1234-1234-123456789125"]["object_data"] = {
    "bbox": [
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
            "name": "bbox-12345689",
            "val": [
                0.42,
                0.480,
                0.58,
                0.626
            ]
        }
    ],
    "boolean": [],
    "text": []
}
with open(output_path, "w") as file_path:
    json.dump(test_json, file_path)