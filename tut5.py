##dictionaries
#dictionary stores data in the form of key:value pair

student = {'name': 'Rohan', 'age': '21', 'courses': ['maths', 'english', 'hindi']}
print (student['courses'])
['maths', 'english', 'hindi']
#to print in a systematic manner
courses_sys = student['courses']

print (courses_sys)


for item in courses_sys:
    print (item)

for index, systematic_order in enumerate(courses_sys, start = 1):
    print (index, systematic_order)

# to get the details

print (student.get('name', 'age'))
print (student.get('phone', 'not found'))
print (student.get('phone'))
print (student.get('something'))
  
student['phone'] = 7054347578
student['name'] = 'Tushar'

student.update({'courses': 'computer science'}) #this will update the courses i.e. replace them
print (student)

#to delete

del student ['age']
print (student)