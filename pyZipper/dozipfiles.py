import zipfile
import os

working_folder = 'C:\\dev\\Testing\\'

for subdir, dirs, files in os.walk(working_folder):
    for file in files:
        print(os.path.join(subdir, file))


files = os.listdir(working_folder)

files_py = []

for f in files:
    if f.endswith('py'):
        fff = os.path.join(working_folder, f)
        files_py.append(fff)

ZipFile = zipfile.ZipFile("zip testing3.cbz", "w" )

for a in files_py:
    ZipFile.write(a, os.path.basename(a), compress_type=zipfile.ZIP_DEFLATED)

#print('Done')



