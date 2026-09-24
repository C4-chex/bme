volumes_str = input("请输入 volumes（用逗号分隔）：")
volumes = [float(x) for x in volumes_str.split(",")]

mi = 0
ma = 0
ima = float(input("上界："))
imi = float(input('下界:'))
for volume in volumes:
    if volume > ima:
        ma +=1
    elif volume < imi:
        mi +=1
print(ma)
print(mi)