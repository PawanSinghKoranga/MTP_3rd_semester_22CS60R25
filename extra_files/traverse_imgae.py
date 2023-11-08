# import the modules
import os
from os import listdir

# get the path/directory
# folder_dir = "F:\iit_kgp_academics\mtp\Running_code\train\MildDemented images"
folder_dir = "trainf" 
for folders in os.listdir(folder_dir):

	# check if the image ends with png
    for images in os.listdir(folder_dir+"\\" + folders):
        if (images.endswith(".jpg")):
            print(images)
