the_variable = "Hello World"
try:
  print(the_variable)
except NameError:
    print("NameError occurred")
except SyntaxError:
    print("SyntaxError occurred")
except:
  print("Something went wrong")
else: # executed if no errors were raised
  print("else statement executed because no errors were raised")
finally:    
    print("finally statement executed no matter what")