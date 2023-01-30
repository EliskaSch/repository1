import argparse
import datetime
from PIL import Image
import os
from os import walk, makedirs, remove
from os.path import isfile, join, exists
from PIL.ExifTags import Base
import shutil


parser = argparse.ArgumentParser(description="Sort images")
parser.add_argument("inputDir", type=str, help="the input directory of images")
parser.add_argument("outputDir", type=str, help="the output directory of images")
parser.add_argument('-x', '--delete', action="store_true", help="deletes the original images")

args = parser.parse_args()

inputDir = args.inputDir
outputDir = args.outputDir
delete_original = args.delete

images = list()

for path, subdirs, files in walk(inputDir):
    for name in files:
        if (isfile(join(path,name))):
            images.append((path,name))
            

sorted_images = {}

for (path,name) in images:
    try:
        with Image.open(join(path,name)) as image_file:
            date = "unknown"
            try:
                data = image_file.getexif()
                date = data[Base.DateTime.value].split(":")[0]
            except:
                print("No exif for " + join(path,name))
            if date in sorted_images.keys():
                sorted_images[date].append((path,name))
            else:
                sorted_images.update({date:[(path,name)]})
    except:
        print(name + " is not an image")
        
        
makedirs(outputDir, exist_ok=True)

for key in sorted_images:
    value = sorted_images[key]
    newDir = join(outputDir, key)
    makedirs(newDir, exist_ok=True)
    for (path,name) in value:
        old_image = join(path,name)
        shutil.copyfile(old_image, join(newDir,name))


folders = os.listdir(outputDir)

for folder in folders:
    if folder == "unknown":
        unknown_directory = os.path.join(outputDir, folder) 
        for count, filename in enumerate(os.listdir(unknown_directory)):
            new_unknown_name = f"{str(count+1)}.jpg"
            old_unknown_name = f"{unknown_directory}/{filename}"
            new_unknown_name = f"{unknown_directory}/{new_unknown_name}"
             
            os.rename(old_unknown_name, new_unknown_name)

for folder in folders:
    if folder != "unknown":
        known_directory = os.path.join(outputDir, folder)   
        
        things = os.listdir(known_directory)
        
        x = 0
        
        for thing in things:
            with Image.open(os.path.join(known_directory, thing)) as img:
                
                img_exif = img.getexif()
                year = img_exif[Base.DateTime.value].split(":")[0]
                month = img_exif[Base.DateTime.value].split(":")[1]
                day_hour = img_exif[Base.DateTime.value].split(":")[2]
                day = day_hour.split()[0]
                           
            old_known_name = os.path.join(known_directory, thing)
            new_known_name = os.path.join(known_directory, year + "-" + month + "-" + day + ".jpg")
            
            if not os.path.exists(new_known_name):            
                os.rename(old_known_name, new_known_name)
            
            if os.path.exists(new_known_name):
                x += 1
                old_known_name_2 = os.path.join(known_directory, new_known_name)
                new_known_name_2 = os.path.join(known_directory, year + "-" + month + "-" + day + "-" + str(x) + ".jpg")
                os.rename(old_known_name_2, new_known_name_2)
        
        
if delete_original:
    answer = input("Do you want to delete the original files? Type y for yes or n for no")
    if answer == "y":
        for f in os.listdir(inputDir):
            os.remove(os.path.join(inputDir, f))
    elif answer == "n":
        pass    