import hashlib
import os
import zipfile


def unpack():
    files = os.listdir('files')
    for file in files:
        if file[-3:] == 'zip':
            dir_name = os.path.join('files/',file[:-4])
            # os.makedirs(dir_name)
            path_zip = os.path.join('files/',file)
            zipOb = zipfile.ZipFile(path_zip)
            zipOb.extractall('files')
            zipOb.close()
            curent_files = os.listdir(dir_name)
            os.chdir(dir_name)
            for cur_file in curent_files:
                if cur_file[-3:] != 'md5':
                    # with open(cur_file, 'r') as f:
                    #     text = f.read()
                    #     text = bytes(text, 'utf-8')
                    #     h = hashlib.md5(text)
                    #     res = h.hexdigest()
                    # with open(cur_file, 'w') as f:
                    #     f.write(res)
            os.chdir('..')
            os.chdir('..')





unpack()

# zip_files = glob.glob('*.zip')
# 
# for zip_filename in zip_files:
#     zip_handler = zipfile.ZipFile(zip_filename, 'r')
#     zip_handler.extractall()