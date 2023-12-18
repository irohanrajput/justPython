def operate(*numbers):  #we don't know the no. of number will be given to us to operate
    print("The sum is: ")
    total = 0
    for num in numbers:
        total += num
    print(total)

    print("The sum is: ")
    product = 1
    for num in numbers:
        product *= num
    print (product)

operate (2,3) 