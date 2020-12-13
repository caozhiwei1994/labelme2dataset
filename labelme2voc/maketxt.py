from sklearn.model_selection import train_test_split
import os

imagedir = 'C:/Users\A\Desktop\labelme-master\data_dataset_voc\JPEGImages/'
outdir = 'C:/Users\A\Desktop/'

images = []
for file in os.listdir(imagedir):
    filename = file.split('.')[0]
    images.append(filename)

train, test = train_test_split(images, train_size=0.8, random_state=0)
val, test = train_test_split(test, train_size=0.1 / 0.2, random_state=0)

with open(outdir + "train.txt", 'w') as f:
    f.write('\n'.join(train))

with open(outdir + "val.txt", 'w') as f:
    f.write('\n'.join(val))

with open(outdir + "test.txt", 'w') as f:
    f.write('\n'.join(test))
