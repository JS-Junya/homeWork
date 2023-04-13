def multi(*num):
    total = 1
    for i in num:
        total = total * i
    return total
print(multi(2,5))
print(multi(2))
print(multi(2,42,5))
print(multi(543,24,62,444))
input()