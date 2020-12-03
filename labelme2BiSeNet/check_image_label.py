from PIL import Image
import numpy as np
img=Image.open('gray/train/000001.png')
img=np.array(img)
a=np.unique(img)
print(a)