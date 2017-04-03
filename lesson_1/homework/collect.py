import hashlib
import os
import zipfile


def unpack():
    files = os.listdir('files')
    print(files)
    for file in files:
        if file[-2] == 'zip':
    	dir_name = join('files/',file[:-4])
    	os.makedir(dir_name)
    	unpack_files = zipfile.ZipFile(file, 'r')
    	unpack_files.extractall()


unpack()

# zip_files = glob.glob('*.zip')
# 
# for zip_filename in zip_files:
#     zip_handler = zipfile.ZipFile(zip_filename, 'r')
#     zip_handler.extractall()