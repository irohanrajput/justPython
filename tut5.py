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
#while using pop in dictionary, minimum 1 arguement is required
#del student ['age']
# print (student)
# popped = student.pop('name')
# print (popped)

print (len(student))
print ("printing all the keys" , student.keys(), "\n", "and now printing all the values", student.values(), "and now printing the items in the dict student", student.items(), "\n")
#here keys() and values() take no arguements

#loop through them

for index, something in enumerate(student, start= 1):
    print (index, something)    #it will only print keys by this method 
    print()
for  key, value in student.items():
    print (key, value)
