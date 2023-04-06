tempStr = input("请输入一串字符：")
lenth = len(tempStr)
alpha , num , space , other = 0 , 0 , 0 , 0
for i in range(lenth):
    if tempStr[i].isdigit() == 1:
        num = num + 1
    elif tempStr[i].isalpha() == 1:
        alpha = alpha + 1
    elif tempStr[i].isspace() == 1:
        space = space + 1
    else:
        other = other + 1
print("这个字符串中有{}个英文字符，{}个数字，{}个空格，{}个其他字符".format(alpha , num , space , other))