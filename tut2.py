#variables, strings 

m = "hello" 
print (m)


#use 3 quotes for multiline strings

message = """this is a multiline 
string"""

#len(string) gives the number of characters in a string


print ("the number of characters is this string is: ") 
print (len(message))

#if total characters = n, then last character is n-1    


print ("the 5th character in the string is: ") 
print (message[5])
print (message[0:5])  #prints all characters from 0 to 4 (exlcuding 5th)
print (message[:5])   #does the same thing        
print (message [6:])  #prints from 6th character to the last 

#note: in [a:b] everytime the last limit will be exluded but in [a:] last limit will be printed too
print (message.upper())

print (message.count("this"))   #print (message.count("arguement")) >> counts the no of times that patricular "arguement is used in the sting"


print (message.find("multiline"))  #prints the character the number from which the arguement "multiline" begins i.e. 10 here..
print ("whatever")


# TO REPLACE A WORD IN A STRING 

message1 = "Nick Fury is dead" 

message2 = message1.replace ("dead", "alive")

print (message1)
print (message2)

#if in case we do not want to create a new variable with replaced word in string, we can use .. message1 = message1.replace("dead", "alive")


message3 = "Nick Fury is Tony's friend "

message4 = message3.replace ("Tony's", "Steve's")

print(message3)
print(message4)
print("\n")



#multiple strings

greeting = "Hii"
name = "Rohan"
msg = greeting + name + "Welcome to this little universe \n"
msg1 = "{} {}, Welcome to this little universe \n".format(greeting, name.upper()) 


#{} this curly brackets act as variable fillers with respective positions.

#{} this curly brackets act as variable fillers with respective positions as in msg1

msg2 = f"{greeting.upper()} {name}, Welcome to this little universe \n"
#we can directly put variables (greeting , name, etc) in the curly brackets after using f'string method as in msg2

print (msg)
print (msg1)
print (msg2)




#to get all available options

# print (dir(name))
# print (help(str))
# print (help(str.lower))

print(message.find("this"))

print ("something again ", message[0])