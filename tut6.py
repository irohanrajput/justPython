
language = 'python' #it's the information we're giving to the system actually, kinda entry

if language == 'python':
    print ('language is python')
elif language == 'java':
    print('language is java')
else:
    print("no match")
#output: language is python


#python doesnt have something  switch case kinda thing...
#object identity: is
#equal: ==
#and
#or
#not

user = 'admin'
logged_in = False   #CHANGE THIS VALUE TO GET DIFFERENT RESULTS

if user == 'admin' and logged_in: #can use 'or' also for alteast one case to satisfy
    print ('welcome to the admin page')
else:
    print('bad creds')

if not logged_in:  #it takes the false statement as true and gives output only if the statement is false
    print('not logged in, please log in')
else:
    print('you are logged in :D')
print("\n")

a = [1,2,3]
b = [1,2,3]
#both are same but 'a' and 'b' have different IDs are two different objects in memory 

print(id(a)) #140005800347584
print(id(b)) #140005778722880

print (a==b)  #true
print (a is b) #false, because 'a' is equal to 'b', but 'a' is not 'b'

#for (a is b ) to be true, we must do.. b = a

# False Values:
    # False
    # None
    # Zero of any numeric type, any other number is true
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping, dictionary For example, {}.

condition = False #using none, 0, '', instead of false is same as that of false

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')