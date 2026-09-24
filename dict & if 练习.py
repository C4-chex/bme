name = input("Enter your name: ")
dict = {'alen':20,
        'bel': 50,
        'bat': 100}
dict.get(name)
print(dict.get(name,"没有你的成绩信息"))
if name in dict:
    if int(dict.get(name)) >= 60 :
        print("合格")
    else :
        print("不合格")

