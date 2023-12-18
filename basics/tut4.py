fruits =  ['apple', 'banana', 'litchi', 'mango']
veg = ['peas', 'potato', 'ladyfinger']

print (fruits ,"\n")

fruits.append('peaches') #adds the item to the list in continuation
print (fruits ,"\n")

fruits.insert(3, "strawberry") #inserts the item in the list to a fixed postion
print (fruits, "\n")

fruits.append(veg) #it adds the new list to the old list but not the items of the list
print (fruits, "\n")

fruits.remove(veg)
print (fruits, "\n")

fruits.extend(veg)  #adds the items of the new list to the old list instead of adding the list itself 
print (fruits, "\n") 

#fruits.pop()  #this removes the last element of the list

fruits.reverse()   #reverse the order of the list
print(fruits)

fruits.sort() #sorts in alphabetical order
#use fruits.sort(reverse) to sort in reverse order