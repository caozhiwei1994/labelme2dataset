import os
from PIL import Image
import numpy as np


def main():
    # 读取原文件夹
    count = os.listdir("before")
    for i in range(0, len(count)):
        # 如果里的文件以jpg结尾
        # 则寻找它对应的png
        if count[i].endswith("jpg"):
            path = os.path.join("before", count[i])
            img = Image.open(path)
            if not os.path.exists('jpg_png/jpg'):
                os.makedirs('jpg_png/jpg')
            img.save(os.path.join("jpg_png/jpg", count[i]))
            # 找到对应的png
            path = "output/" + count[i].split(".")[0] + "_json/label.png"
            img = Image.open(path)
            # 找到全局的类
            class_txt = open("class_name.txt", "r")
            class_name = class_txt.read().splitlines()
            # ["_background_","a","b"]
            # 打开json文件里面存在的类，称其为局部类
            with open("output/" + count[i].split(".")[0] + "_json/label_names.txt", "r") as f:
                names = f.read().splitlines()
                # ["_background_","b"]
                new = Image.new("RGB", [np.shape(img)[1], np.shape(img)[0]])
                # print('new:',new)
                for name in names:
                    index_json = names.index(name)
                    index_all = class_name.index(name)
                    # 将局部类转换成为全局类
                    new = new + np.expand_dims(index_all * (np.array(img) == index_json), -1)
            new = Image.fromarray(np.uint8(new))
            print('new:',new)
            if not os.path.exists('jpg_png/png'):
                os.makedirs('jpg_png/png')
            new.save(os.path.join("jpg_png/png", count[i].replace("jpg", "png")))
            print(np.max(new), np.min(new))

if __name__ == '__main__':
    main()
