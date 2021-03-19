a=5
b=9
c=a+b
print(c)
import pandas as pd
#tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img

a=load_img(r'C:\Users\user\Downloads\cotton leaf disease prediction\test-20210106T035653Z-001\test\fresh cotton leaf\d (366)',
           target_size=(224,224))