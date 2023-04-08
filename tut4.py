#lists, tuples, and sets
courses = ['history', 'physics', 'maths', 'english', 'chemistry']



print (len(courses))

print (courses[-1]) #prints the last item of the index

print (courses[0])

print (courses[0:]) #prints from the first item to the last item.. same rule as of in strings

print (courses[0:-1]) #prints everything excluding the last item

#learn slicing, link: tut4, 5:18 duration 

#to add something to the list (in continuation )

courses.append('adding new values')

#insert an item to a fixed position
#list.insert(desired position, 'value')

courses.insert(3, "added at the 4th position") #*it starts from 0

print (courses)


courses_2 = ['new', 'list']

courses.insert(2, courses_2)
print (courses)
['history', 'physics', ['new', 'list'], 'maths', 'english', 'chemistry']

#but we want to add the items of the list, not the list itself
print("\n\n\n")

courses.extend(courses_2)
print (courses)

courses.remove(courses_2)
courses.remove(courses_2)




