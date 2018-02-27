import numpy as np
import h5py
import io
import os


class FileHelper(object):

    def __init__(self, db):
        self.db = h5py.File(db)

    def get(self):
        return self.db

    def StoreFile(self, Path, StorePath, **mataData):
        ImageFile = open(Path, 'rb')
        try:
            dt = h5py.special_dtype(vlen=np.dtype('uint8'))
            temp = self.db.create_dataset(StorePath, (1,), dtype=dt)
        except Exception as e:
            temp = self.db[StorePath]

        temp[0] = np.fromstring(ImageFile.read(), dtype='uint8')
        

    def StoreFromFolder(self, Path, savePath=""):

        directory = os.fsencode(Path)
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            self.StoreFile(Path + filename, savePath + filename)

    def List(self, Path):
        return [key for key in self.db[Path].keys()]

