# -*- coding: utf-8 -*-
"""RGB_to_Grayscale.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ekSUc4Jku3WEq0t4j5Mz7IYhc4_z7_pR
"""

import tensorflow as tf
import numpy as np
import pandas as pd

train = np.load('drive/MyDrive/train.npy')

train.shape

split = np.array_split(train, 10)

converted_data = []

for chunks in split:
  converted_data.append(tf.image.rgb_to_grayscale(chunks))

train_gray = np.concatenate(converted_data, axis=0)

np.save('drive/MyDrive/train_gray.npy', train_gray)