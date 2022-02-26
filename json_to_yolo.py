"""
@author: Muhammad Hanan Asghar
"""

# libraries
import json
import time
import os


def convert(source_path, destination_path):
    with open(source_path) as json_file:
        data = json.load(json_file)

        print("Converting...\n")
        counter = 0

        for p in data['annotations']:
            if counter > 0 and counter % 1000 == 0:
                print("Converted: {0} images".format(counter))  
            for p in data['annotations']:
                if (p['image_id'] == counter):
                    print(p['category_id'], end=" ", file=open(destination_path +'/FLIR_0{:04d}.txt'.format(counter + 1), 'a'))
                    print((p['segmentation'][0][0] + p['segmentation'][0][4])/ 2 / 640, end=" ", file=open(destination_path + '/FLIR_0{:04d}.txt'.format(counter + 1), 'a'))
                    print((p['segmentation'][0][1] + p['segmentation'][0][3]) / 2 / 512, end=" ", file=open(destination_path + '/FLIR_0{:04d}.txt'.format(counter + 1), 'a'))
                    print(p['bbox'][2] / 640, end=" ", file=open(destination_path + '/FLIR_0{:04d}.txt'.format(counter + 1), 'a'))
                    print(p['bbox'][3] / 512, file=open(destination_path + '/FLIR_0{:04d}.txt'.format(counter + 1), 'a'))
            counter += 1
            if (counter >= int(p['image_id'])):
                print("Total: {0} images converted\n".format(counter))
                print("Conversion successfully!" )
                break
    return None    


def main():
    source_path = "val_thermal_annotations.json"
    destination_path = "val_images"
    convert(source_path, destination_path)

if __name__ == "__main__":
    main()
