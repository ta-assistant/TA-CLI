import os

A = "C:/Users/detec/Documents/Grid"
path = A
zip = os.listdir(path)
count = 0
print(zip)

for i in zip :
    count += 1
print(count)

from file_management_lib import DirManagement

create_dir = DirManagement().create_dir

import zipfile

for i in zip:
    name = A+f"/{i}"
    folder = name[0:-4]
    print(name,folder)
    with zipfile.ZipFile(name) as my_zip:
        create_dir(folder)
        my_zip.extractall(folder)
        my_zip.close()


#with zipfile.ZipFile(r"C:\Users\detec\Documents\Grid\Files.zip") as my_zip:
#    create_dir(r"C:\Users\detec\Documents\Grid\Files")
#    my_zip.extractall(r"C:\Users\detec\Documents\Grid\Files")
#    my_zip.close()

    