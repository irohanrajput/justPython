# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result

# my_nums = square_numbers([1,2,3,4,5])

# print (my_nums)

def square_numbers(nums):
    length = len(nums)
    for i in nums:
        yield(i*i)

my_nums = square_numbers([1,2,3,4,5])

print (next(my_nums))
print ("after printing the first value, it starts from the second value")

for i in my_nums:
    print(i)
