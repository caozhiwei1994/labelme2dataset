import os


def write_txt(type,txt):
    gt = os.listdir("dataset/gt_png/"+type)
    label = os.listdir("dataset/label_png/"+type)
    with open(txt, "w") as f:
        for i in gt:
            j = i.replace("gt_png","label_png")
            # 判断jpg是否存在对应的png
            if j in label:
                f.write("gt_png/"+ type + '/' + i + ","+"label_png/"+type + '/'+ j + "\n")

write_txt("train","train.txt")
write_txt("val","val.txt")
