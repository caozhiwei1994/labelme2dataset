# resize.py
import cv2
import os
import shutil


def main(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.png'):
                image_name = os.path.join(root, file)
                image = cv2.imread(image_name, -1)
                crop_image = cv2.resize(image,(1080,704))
                os.remove(image_name)
                cv2.imwrite(image_name, crop_image)

image_path = './dataset/gt_png'
label_path = './dataset/label_png'
if __name__ == '__main__':
    main(image_path)
    main(label_path)

