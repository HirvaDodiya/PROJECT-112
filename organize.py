import os
import shutil

from_dir="C:/Users/LENOVO/Downloads"
to_dir="C:/Users/LENOVO/Desktop/organizer"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for x in list_of_files:
    name,extension = os.path.splitext(x)
    if extension == "":
        continue
    if extension in [".gif",".png",".jpeg","jpg","jfif"]:
        path1 = from_dir+"/"+x
        path2 = to_dir+"/"+"Image_files"
        path3 = to_dir+"/"+"Image_files"+"/"+x

        if os.path.exists(path2):
            print("Moving"+x)
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving"+x)
            shutil.move(path1,path3)
        