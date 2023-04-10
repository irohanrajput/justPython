#for loop

nums = [1,3,2,4,7,5,6,8]
nums.sort()

print("here the list is ", nums)

for num in nums:
    if num == 3:  #ek ek kar ke check krte hue 3 tak pohochega and then the process
        print("found the number 3 and breaking the loop no")
        break  
    print(num)

print("\n")

for num1 in nums:
    if num1 == 3:  
        print("number 3 was found and it is now continuing ahead") 
        continue 
    print(num1)

for num in nums:
    for letter in 'abc':
        print (num, letter) #every number in nums will loop through every letter in abc i.e. 1-a,b,c..2-a,b,c and so on 


ran = range(10)
for i in ran:
   print (i) #range 10 denotes num from 0 to 9
print("\n")
for j in range(1,11):
    print(j)