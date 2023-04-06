inputNum = eval(input("请输入一个整数N:"))
sum = 0
for i in range(inputNum+1):
    sum = sum + i 
print("1~{}相加的和为{}".format(inputNum,sum))