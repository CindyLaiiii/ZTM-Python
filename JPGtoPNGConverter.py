
# import required module
import sys
import os
from PIL import Image, ImageFilter

# 在terminal
# 輸入: python3 JPGtoPNGConverter.py pokedex eee

# 從terminal抓取檔名
arg1 = str(sys.argv[1]) #pokedex
arg2 = str(sys.argv[2]) #eee

# new folder的路徑
fullpath = arg1+"/"+arg2

# check if folder exist
if os.path.isdir(fullpath):
    print("exist")

else:
	print("Creat a directory")

	# if not exist create folder
	os.mkdir(fullpath)

# 欲提取照片的folder name
directory = arg1

# loop all files in the folder
for filename in os.listdir(directory):
    if filename.endswith('.jpg'):

    	# extract filename
        f = os.path.join(directory, filename)

        # open image
        img = Image.open(f)


        # change file name end in .png
        filename = filename.replace("jpg","png")


        # save and chang format
        img.save(directory+f"/{arg2}/"+filename,format = "png")

# 參考網址：
# check-if-file-exists
# https://www.python-engineer.com/posts/check-if-file-exists/
# Iterate Over Files in a Directory Using Python
# https://pieriantraining.com/iterate-over-files-in-directory-using-python/

