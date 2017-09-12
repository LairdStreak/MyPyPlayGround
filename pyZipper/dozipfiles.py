import zipfile
import os

working_folder = 'D:\\Nisekoi\\'

for dirName, subdirList, fileList in os.walk(working_folder):
    ZipFile = zipfile.ZipFile(dirName + "_.cbz", "w" )
    #print('Found directory: %s' % dirName)
    for fname in fileList:
     #   print('\t%s' % fname)
        ZipFile.write(os.path.join(dirName,fname), fname, compress_type=zipfile.ZIP_DEFLATED)

print('done')        
        #//print(os.path.join(dirName,fname))
#for subdir, dirs, files in os.walk(working_folder):
#    for dir in dirs:
#        print(os.path.join(subdir, dir))
    #for file in files:
    #    print(os.path.join(subdir, file))

#for name in dirs:
#        print(os.path.join(root, name))
#files = os.listdir(working_folder)

#files_py = []

#for f in files:
#    if f.endswith('py'):
#        fff = os.path.join(working_folder, f)
#        files_py.append(fff)

#ZipFile = zipfile.ZipFile("zip testing3.cbz", "w" )

#for a in files_py:
#    ZipFile.write(a, os.path.basename(a), compress_type=zipfile.ZIP_DEFLATED)

#print('Done')



