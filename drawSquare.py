def line1():
    for i in range(21):
        if i==0 or i==10 or i==20:
            print("+", end='')
        elif i%2==0:
            print("—", end='')
        else:
            print("  ", end='')
    print()
def line2():
    for i in range(21):
        if i==0 or i==10 or i==20:
            print("|", end='')
        else:
            print("  ", end='')
    print()
for a in range(21):
    if a==0 or a==10 or a==20:
        line1()
    elif a%2==0:
        print()
    else:
        line2()