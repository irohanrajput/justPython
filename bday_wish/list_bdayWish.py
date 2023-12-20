from num2words import num2words

i = 1
kids_list = []

while True:
    kidName = input(f"Enter the name of the {num2words(i, ordinal=True)} kid: ")
    if len(kidName) != 0:
        kids_list.append(kidName)
        i +=  1
    else:
        break
for kid in kids_list:
    print(f"Happy b'day {kid}")
    with open("bdayWishes.txt", "a+") as savedata:
            savedata.write(f"Happy birthday {kid}\n")

