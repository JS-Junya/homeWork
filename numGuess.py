from random import randint
randNum = randint(0,9)
N=100
for i in range(N):
    try:
        inputNum = eval(input("请输入一个整数："))
    except:
        print("输入错误")
        break
    if inputNum < randNum:
        print("遗憾，太小了")
    elif inputNum > randNum:
        print("遗憾，太大了")
    else:
        print("预测{}次，你猜中了！".format(i+1))
        break
input()