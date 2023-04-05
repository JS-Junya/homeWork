while True:
    TempStr=input("请输入要判断的三位数(输入exit退出):")
    if TempStr=="exit":
        break
    if TempStr.isdigit()==1:
        if len(TempStr)==3:
            a=int(TempStr[0])
            b=int(TempStr[1])
            c=int(TempStr[2])
            if a**3+b**3+c**3==eval(TempStr):
                print("{}是水仙花数".format(TempStr))
            else:
                print("{}不是水仙花数！".format(TempStr))
        else:
            print("{}不是三位数！！".format(TempStr))
    else:
        print("{}不是正整数！！！".format(TempStr))