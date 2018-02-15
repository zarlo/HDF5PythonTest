from PIL import Image
import numpy as np
import h5py
import six
import io
import os
#h5py.run_tests()
f = h5py.File('TestFile.hdf5')

#this lets you store data
def StoreFile(Path, StorePath):
    ImageFile = open(Path, 'rb')
    try:
        dt = h5py.special_dtype(vlen=np.dtype('uint8'))
        temp = f.create_dataset(StorePath,(1,) , dtype=dt)
    except Exception as e:
        temp = f[StorePath]

    temp[0] = np.fromstring(ImageFile.read(), dtype='uint8')


#lets you store data from a folder
def StoreFromFolder(Path, savePath = -1):

    if savePath is -1:
        savePath = Path
    directory = os.fsencode(Path)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        StoreFile(Path + filename, savePath + filename)


def List(Path):
    return [key for key in f[Path].keys()]


StoreFromFolder('data/', '/a_place/')


StoreFile('im1.jpg', '/cats/im1.jpg')
StoreFile('im2.jpg', '/cats/im2.jpg')
StoreFile('im3.jpg', '/cats/im3.jpg')

workPath = "/"

print(List('/'))

while True:
    path = input(workPath + ':>')
    if path.startswith('/'):
        workPath = path
    else:
        workPath += path

    print(List(workPath))
