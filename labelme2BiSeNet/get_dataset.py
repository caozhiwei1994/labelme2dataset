import cv2
import os
from PIL import Image

#if picture is jpg,you can use jpg2png
jpg_read = "jpg_png/jpg/"
if not os.path.exists('dataset/gt_png'):
    os.makedirs('dataset/gt_png')
png_write = "dataset/gt_png/"
jpg_names = os.listdir(jpg_read)
for j in jpg_names:
    img = Image.open(jpg_read + j)
    j = j.split(".")
    if j[-1] == "jpg":
        j[-1] = "png"
        j = str.join(".", j)
        # r,g,b,a=img.split()
        # img=Image.merge("RGB",(r,g,b))
        to_save_path = png_write + j
        img.save(to_save_path)
    else:
        continue

#24bit to 8bit
bit24_dir = 'jpg_png/png'      #上一步保存.png图像文件夹
if not os.path.exists('dataset/label_png'):
    os.makedirs('dataset/label_png')
bit8_dir = 'dataset/label_png'
png_names = os.listdir(bit24_dir)
for i in png_names:
    img = cv2.imread(bit24_dir+'/'+i)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imencode('.png', gray)[1].tofile(bit8_dir+'/'+i)


