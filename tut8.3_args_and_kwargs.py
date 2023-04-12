#  https://youtu.be/0lu2SY3menU

#*args tuple ke form me jata hai, ** =kwargs dictionary k form me
#they are used to put entries if we don't know the no. of entries

def func(normal_statement = 'welcome', *args, **kwargs):
    for index, item in enumerate(args, start = 1):
        print(index, item , "\n")
    for key1, value1 in kwargs.items():
        print('{} is {}'.format(key1, value1)  )

some1 = ['Rohan', 'Mohan', 'David']
some2 = {'Mogambo': 'Villian', 'Surya': 'Don', 'RCB': 'Love'}
    

print(func('normal_statement', *some1, **some2))