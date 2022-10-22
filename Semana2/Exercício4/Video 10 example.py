import os
from datetime import datetime

os.makedirs('OS-Demo/Sub-Dir-1')

os.chdir('OS-Demo/Sub-Dir-1')

f = open('teste.txt','w+')

print(os.listdir())

f.close()

os.rename('teste.txt', 'demo.txt')

print(os.listdir())

time = os.stat('demo.txt').st_mtime

print(datetime.fromtimestamp(time))

os.remove('demo.txt')

os.chdir('../..')

print(os.listdir())

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)

print(os.environ.get('HOMEPATH'))

file_path = os.path.join(os.environ.get('HOMEPATH'), 'teste.txt')
print(file_path)

os.path.exists('teste.txt')

os.path.splitext('teste.txt')

os.removedirs('OS-Demo/Sub-Dir-1')