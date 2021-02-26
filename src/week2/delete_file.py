import os

file_name = '/home/srujan/Desktop/logs/2021-02-26 07:38:33.335343.txt'
if os.path.exists(file_name):
    os.remove(file_name)
else:
    print('File not present')

file_count = '2021-02-26 07:38:34.964324.txt'
if os.path.exists(file_count):
    os.remove(file_count)

del_dir = '/home/srujan/Desktop/logs/'
for file in os.listdir(del_dir):
    if '.txt' in file:
        os.remove(del_dir+file)
    appendPath = del_dir+file+'/'
    if os.path.exists(appendPath):
        print(appendPath)
        for files in os.listdir(appendPath):
            if '.txt' in files:
                os.remove(appendPath+files)




