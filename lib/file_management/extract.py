#from file_management_lib import FlieManagement

#class ExtractFile(FlieManagement):
#    pass

import zipfile

with zipfile.ZipFile(r"C:\Users\detec\Documents\Grid\Files.zip") as my_zip:
#    print(my_zip.namelist())
#    my_zip.extractall(r"C:\Users\detec\Documents\Grid\Unzip")
#    my_zip.extractall(r"C:\Users\detec\Documents\Grid")
    my_zip.extractall("Files")
    my_zip.close()

#target = C:\Users\detec\Documents\Grid\Files.zip
#handle = zipfile.ZipFile(target)
#handle.extractall()
#handle.close()