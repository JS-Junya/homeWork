try:
    inputNum = eval(input("请输入一个整数N:"))
except:
    print("输入错误")
sum = 0
for i in range(inputNum+1):
    sum = sum + i 
print("1~{}相加的和为{}".format(inputNum,sum))