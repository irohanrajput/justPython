#loops and iterations (for, while)

nums = [1,3,2,4,7,5,6,8]
nums.sort()

print("here the list is ", nums)

for num in nums:
    if num == 3:  
        print("found the number 3 and breaking the loop no")
        break  #prints everything before 3
    print(num)

print("\n")

for num1 in nums:
    if num1 == 3:  
        print("number 3 was found and it is now continuing ahead") 
        continue 
    print(num1)

for num in nums:
    for letter in 'abc':
        print (num, letter) #every number in nums will loop through every letter in abc