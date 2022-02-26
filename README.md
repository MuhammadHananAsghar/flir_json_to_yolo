# FLIR JSON TO YOLO

## About
This script extract informations about annotations from FLIR thermal_annotations.json file and transfer it into the text files. Each text file consists of annotations about one image.
The format is:

[c, bx, by, bw, bh]

c - class
bx - box center coordinate x / image width
by - box center coordinate y / image height
bw - box width / image width
bh - box height / image height

# FLIR JSON TO CLASSES
Convert flir json annotations to classes.txt for Yolo Versions.
