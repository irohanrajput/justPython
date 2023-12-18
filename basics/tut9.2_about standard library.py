import random

courses = ['History', 'Math', 'Physics', 'CompSci']

random_subject = random.choice(courses)
print (random_subject)


import math
pie = math.pi
print(math.sin(pie/2))

print('\n','now calling the function', '\n')

def sinwd(deg):
    rad = math.radians(deg)
    print (math.sin(rad))

def coswd(deg):
    rad = math.radians(deg)
    print (math.cos(rad))

sinwd(30)

import datetime
today = datetime.date.today()
print (today) and print (time)


import calendar

def leap(year):
    print(calendar.isleap(year))

leap (2020)

import os

#The OS module gives us ability to scan, modify, delete files etc

print (os.getcwd())  #gets us the current working directory

print('7.',os.__file__)

