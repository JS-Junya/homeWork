from math import *
def isNum(num):
    try:
        num = eval(num)
        if type(num)==int or type(num)==float or type(num)==complex:
            return True
    except:
        return False
while True:
    print(isNum(input()))