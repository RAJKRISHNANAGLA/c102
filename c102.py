import os
import shutil
source='C:/users/rajkr/downloads'
destination='C:/users/rajkr/onedrive/desktop'
files=os.listdir(source)
#print(files)
for file in files:
    n,e=os.path.splitext(file)
  # print(n)
  # print(e)
    if e=="":
        continue
    if e in ['.txt','.pdf','.doc','.docx']:
        path1=source+'/'+file
        path2=destination+'/'+'krishna'
        path3=path2+'/'+file
        if os.path.exists(path2):
            print('moving '+file+'...')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('moving '+file+'...')
            shutil.move(path1,path3)
