"""
@author: Muhammad Hanan Asghar
"""

# Libraries
import os
import json
import time


def convert_to_classes(source_path):
    with open(source_path) as json_file:
        data = json.load(json_file)
        with open("classes.txt", "w") as txt:
            for item in data['categories']:
                txt.write(item['name']+'\n')
    txt.close()
    
if __name__ == "__main__":
	source_path = "thermal_annotations.json"
	convert_to_classes(source_path)
