# we can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword.

# Example
# Raise an error and stop the program if x is lower than 0:

x = 1
if x < 0:
  raise Exception("exception raised, as x is less than zero")
else:
    print("\nNo exceptions raised in the first program, passing onto second. \n")
    pass
    

#defining the type of exception to be raised

a = 'hello'

if not type(a) is int:
    raise TypeError("Only integers are allowed")
else:
    print("all good")
