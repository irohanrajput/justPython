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


