setNum = 6
for i in range(10):
    inNum = eval(input("请输入一个整数："))
    if inNum < setNum:
        print("遗憾，太小了")
    elif inNum > setNum:
        print("遗憾，太大了")
    else:
        print("预测{}次，你猜中了！".format(i+1))
        break
