# limit = int(input("enter the limit: "))
limit = 10


def fibs(last_digit):
    a = 0
    b = 1
    print(a, end=' ')

    for i in range(last_digit):
        nextnum = a + b
        yield nextnum
        a = b
        b = nextnum

series = fibs(limit)
for i in series:
    print(i, end=' ')
