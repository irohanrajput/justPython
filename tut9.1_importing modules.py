
courses = ['History', 'Math', 'Physics', 'CompSci']
import sys
sys.path.append("/home/irohanrajput/Desktop/Work/Python/Modules")
#if in case, you don't want to fill the root folder with libraries and modules.. create a folder for it and attach it to the project file like this

import my_module as mm   #use shorter name

details = mm.find_index_with_name(courses, 'Math') #we  need to assign first because in this example we didn't imported the function but module 
print ('6.',details)
testst = mm.test
print ('8.',testst)

print('\n\n now prting each item separately. \n')
#we can directly import the function from the module
from my_module import find_index_with_name as fin, test

print(fin(courses, 'Math'))
print ('15.',test)

#importing this way only imports the mentioned thing
#to access everything in the module, we use 'from my_module import *

import sys
print (sys.path) #to know the locations where python looks for modules



