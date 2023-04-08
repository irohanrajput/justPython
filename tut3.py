#NUMERIC DATA IN PYTHON
#floats and integers
num  = 3
num2 = 3.14
print(type(num)) #this gives the type of data of "num"
print(type(num2))

#arithemetic operators
print (3+2) #addition
print (3-2) #subtraction    
print (2-3) #subtraction with a negative result
print (3*2) #multiply
print (3/2) #division
print (2/3) #division where den > num
print (3 // 2) #floor division (it eliminates the decimal value)
print (7**2) #exponent
print (7%3)  #to get the remainder

print ("\n increament in values")


#python follows BODMAS

num  = 2
print (num)
num += 3  #value of num has become 2+3= 5 now
print (num)
num *=3 #value of num has become 5x3 = 15 now
print (num) 

print(abs(-3))

#round off
print(round(2/3, 2)) #here putting 2 means it will round of the result to second decimal point

float = 2/3
result = f"{float:.3f}" #will print to the 2nd decimal point
print(result)

#comparison operators
#equal:       a==b
#not equal :  a!=b
#grter than:  a>b
#less than:   a<b
#greater or equal : a>=b
#smaller or equal : a<=b
num3=3
num4=4
print(num3==num4)   #output : False
print(num3<num4) #output : True



#casting from strings to variables

num5 = "4"
num6 = "7"

#casting

num5 = int(num5)
num6 = int(num6)
print ( num5 + num6) #output = 11

