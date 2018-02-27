from hdf5helper import *

f = FileHelper('TestFile.hdf5')

f.store_from_folder('data/', '/a_place/')
f.store_file('im1.jpg', '/cats/im1.jpg')
f.store_file('im2.jpg', '/cats/im2.jpg')
f.store_file('im3.jpg', '/cats/im3.jpg')
workPath = "/"

print(f.list('/'))

while True:
    path = input(workPath + ':>')
    if path.startswith('/'):
        workPath = path
    else:
        workPath += path

    print(f.list(workPath))
