#the string  "once upon a time there was an idea to bring the group of remarkable people together", is given..
#WAP to print the string in reverse order


st1 = "once upon a time there was an idea to bring the group of remarkable people together"
print (st1)

st1_as_list = st1.split(" ")
print (st1_as_list)
print ("\n")
print ("\n")

st1_as_list.reverse()
st1_in_reverse = " ".join(st1_as_list)
print ("\n")
print ("printing the string as it is:", st1)
print ("\n")
print ("printing the string in reverse:",st1_in_reverse)
