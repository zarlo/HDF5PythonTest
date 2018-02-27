import numpy as np
import h5py
import io
import os
from hdf5helper import *


f = FileHelper('TestFile.hdf5')


f.StoreFromFolder('data/', '/a_place/')
f.StoreFile('im1.jpg', '/cats/im1.jpg')
f.StoreFile('im2.jpg', '/cats/im2.jpg')
f.StoreFile('im3.jpg', '/cats/im3.jpg')
workPath = "/"

print(f.List('/'))

while True:
    path = input(workPath + ':>')
    if path.startswith('/'):
        workPath = path
    else:
        workPath += path

    print(f.List(workPath))
