while True:
    try:
        year = eval(input("请输入要判断的年份："))
    except:
        print("输入错误")
        continue
    if year % 4 == 0 and year % 100 != 0:
        print("{}年是闰年".format(year))
    elif year % 400 == 0:
        print("{}年是闰年".format(year))
    else:
        print("{}年不是闰年".format(year))
input()
