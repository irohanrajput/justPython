#sorting with numbers
nums  = [1,3,5,7,6,4,0]
nums.sort(reverse= True)  #by default, it sorts in ascending order but using reverse sorts it in descending order
print ("printing the first list:", nums)

num2=[1,4,6,8,3,6,9,4]
num2_asc = sorted(num2) #using sorted function for new sorted list without alternig the original one

print ("printing the second list in ascending order:", num2_asc)

num2_des = sorted(num2)
num2_des.sort(reverse=True)
print("printing the second list in descending order:", num2_des)


print (min(nums))  #min, max, sum

print (max(nums))
print (sum(nums))

print (num2.index(6)) #to get the location of 6 in the list


print (6 in num2) #check if the value is in the list or not

#for loop

courses = ["maths", "english", "hindi"]


#for item in list:
     #print (item)
 
for item in courses:
    print (item)


for index, item2 in enumerate(courses, start = 1):  #if we want numbering too i.e. index #enumerate


    print(index, item2)

#to separate each value of the list and put them as a string with commas b/w them

course_str = " and ".join(courses)
print(course_str)

#to separate the values of a string as a list
string = "my name is Rohan Rajput"
new_list = string.split(' ')
print (new_list)

#tuples are not mutable i.e. they does not support item assignment

tuple_1 = ('history', 'math', 'physics', 'CompSci')
tuple_2 = tuple_1
print (tuple_1)
print (tuple_2) 

#tuple_1[0] = 'art'
#print(tuple_1)    this will give an error as we can't modify the items in a tuple

#use list when you want to modify something later and use tuple when u don't want the the items to be modified

#sets don't really care about order, they throw away duplicates i.e. if the we put two same items in a set, it'll print only one and will throw away the other

#sets do follow intersection, difference, union etx.

cs_courses = {'History', 'Math', 'Physics', 'CompSci',}
art_courses  = ['pol sci', 'history', "civics", 'CompSci']

print ("the union of all subject is:", cs_courses.union(art_courses),"\n")
print ( "the common subjects among the both lists are:", cs_courses.intersection(art_courses),"\n")
print ( "the different subjects among the both lists are:",cs_courses.difference(art_courses),"\n")

sub_union = cs_courses.union(art_courses)
print ("total subjects available are:")
for item3 in sub_union:
    print (item3)     # *..*



# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dictionary
empty_set = set()

