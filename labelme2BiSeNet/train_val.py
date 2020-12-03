# train_val.py

'''
将数据分为train val
'''

import os
import random
import shutil

total_list = []
train_list = []
val_list = []


image_path = 'dataset/gt_png'
label_path = 'dataset/label_png'

# 清空
for dir in ['train', 'val']:
    image_dir = os.path.join(image_path, dir)
    label_dir = os.path.join(label_path, dir)
    if os.path.exists(image_dir):
        shutil.rmtree(image_dir)
    os.makedirs(image_dir)
    if os.path.exists(label_dir):
        shutil.rmtree(label_dir)
    os.makedirs(label_dir)


for root, dirs, files in os.walk(image_path):
    for file in files:
        if file.endswith('png'):
            total_list.append(file)

total_size = len(total_list)
train_size = int(total_size * 0.8)
val_size = total_size-train_size

train_list = random.sample(total_list, train_size)
remain_list = list(set(total_list) - set(train_list))
val_list = random.sample(remain_list, val_size)



for file in total_list:
    image_path_0 = os.path.join(image_path, file)
    label_file = file.split('.')[0] + '.png'
    label_path_0 = os.path.join(label_path, label_file)
    if file in train_list:
        image_path_1 = os.path.join(image_path, 'train', file)
        shutil.move(image_path_0, image_path_1)

        label_path_1 = os.path.join(label_path, 'train', label_file)
        shutil.move(label_path_0, label_path_1)

    elif file in val_list:
        image_path_1 = os.path.join(image_path, 'val', file)
        shutil.move(image_path_0, image_path_1)

        label_path_1 = os.path.join(label_path, 'val', label_file)
        shutil.move(label_path_0, label_path_1)


print(len(total_list))
print(len(train_list))
print(len(val_list))