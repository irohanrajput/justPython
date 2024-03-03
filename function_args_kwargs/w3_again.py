list = ["apple", "banana", "cherry"]

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# *args: in the form of tuples
# **kwargs: in the form of dictionary
# default parameter in function

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")   # I am from Sweden
my_function("India")    # I am from India
my_function()           # I am from Norway
my_function("Brazil")   # I am from Brazil