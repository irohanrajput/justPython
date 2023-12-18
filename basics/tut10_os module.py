import os
print(dir(os)) #  it shows all attributes and methods that we have access in this module
print(os.getcwd())

os.chdir('/home/irohanrajput/Desktop/My Stuff')
print(os.getcwd(), "current dir")

print (os.listdir())

os.chdir('/home/irohanrajput/Desktop')

os.mkdir('new demo')  #to create single folder
os.makedirs('new demo 2/ within demo 2/within it')

os.mkdir('new demo')  #to create single folder
os.rmdirs('new demo 2/ within demo 2/within it') # avoid using it

print(os.getcwd(), "current dir")

os.rename('token.txt', 'toKen.txt')

print(os.stat('toKen.txt').st_size)
from datetime import datetime
mod_time = (os.stat('toKen.txt').st_mtime)
print(datetime.fromtimestamp(mod_time))   #to get in human readable form

#printing everything in the dir

for main_folder, folders_inside_main_folder, file_in_the_current_folder in os.walk('/home/irohanrajput/Desktop'):
    print('current location: ', main_folder)
    print('folders inside main folder: ', folders_inside_main_folder)
    print('files in the current dir: ', file_in_the_current_folder)

print('new...', os.environ.get('HOME')) 
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
