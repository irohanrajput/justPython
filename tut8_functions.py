# def is used to define functions


def hello_func():
    print('calling the function')

# now we don't need to print the function, we can call it directly because print is already declared in the function itself

hello_func() #this will call the function which is to print something

#but what if we want to define a funtion but don't really want to print it as of now

def hello_func2():
    return "this won't print the string without using the print command"
hello_func2() #this will give nothing
print('16.',hello_func2()) #this will do the printing thing


print('19.',hello_func2().upper())

#CREATING A PARAMETER FOR FUNCTION

def hello_funcp(greeting):
    return '{} people.'.format(greeting) #the return value and 

print (hello_funcp('26. hii'))  #here we are putting in the entry of greeting as "hii"

def hello_funcn(greeting = 'hii', name = "rohan"): #default grt is hii and default name is rohan 
    return'{} {}, this is how we use arguements is functions'.format(greeting, name)

print(hello_funcn('30. hello again', 'rohan')) #here we gave the input for greeting and name so it printed as it is
print(hello_funcn()) #here we didn't gave the input fot greeting and name so it printed the default value

# for unknow things 
# single star * represent a list, double star ** represents a dictionary

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['math', ]

student_info ('math', 'art', name = 'john', age = 22)
