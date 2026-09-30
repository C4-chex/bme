import tkinter as tk

from decimal import Decimal
from functools import partial
from tkinter import messagebox
window = tk.Tk()
window.title('计算器')
#这里发现要先设置geometry尺寸再mainloop
window.geometry('400x600')
window2 =tk.Toplevel(window)
window2.geometry('100x400')

#显示框
display = tk.Entry(window,  justify='right')
display.grid(row=0, column=0, columnspan=4,rowspan=2,sticky='nsew', padx=5, pady=5)

#按钮1
nums = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['0', '.', 'C'],
]
#按钮2
cha = [
    ['+'],
    ['-'],
    ['*'],
    ['/'],
    ['='],
    ['<-']
]
L1 = ['*','/','+','-']
L2 = ['*','/']
fir = []


def press(text):
    if text == 'C':#处理归零
        display.delete(0, tk.END)
        fir.clear()
    elif text == '<-':#处理delete
        delete(text)
    elif text == '=':#处理求和
        calculate_t(text)
    else :
        if text != 'C' and text != '<-':#处理连续符号
        # for i in range(1, len(fir)):
        #         if fir[i] in L1 and fir[i - 1] in L1:
        #             delete(text)
        #             messagebox.showerror('错误', 'ERROR')
        #             return
        #     if fir[0] in L2:#处理符号开头
        #         messagebox.showerror('错误', 'ERROR')
        #
        # display.insert(tk.END, text)
        # calculate(text)
                #处理双符号
            if text in L1 and fir and fir[-1] in L1:
                if text == '-':
                    pass
                else:
                    messagebox.showerror('错误', 'ERROR')
                return
                # 检查符号开头
            if not fir and text in L2:
                messagebox.showerror('错误', 'ERROR')
                return
            display.insert(tk.END, text)
            calculate(text)





# def delete(text):
#     display.delete(len(display.get())-1 , tk.END)
#     fir.pop(len(display.get()) )
#     print(fir)

def delete(text):
    if not fir:
        return
    display.delete(len(display.get()) - 1, tk.END)
    fir.pop()
    print(fir)
def calculate(text):
    fir.append(text)
    print(fir)




def calculate_t(text):
    shu1 = []
    las = ''

#     for shu in fir:
#         if shu in '0123456789.':
#             las += shu
#         else:
#             shu1.append(Decimal(las))
#             shu1.append(shu)
#             las = ''
#     if las:  # 防崩
#         shu1.append(Decimal(las))


    # for i in shu1:
    #     while i =='*' or i =='/':
    #         return shu1[i-1]


    for i,shu in enumerate(fir, start=1):
        if shu in '0123456789.':
            las += shu
        elif shu == '-' and (i==0 or fir[i-1] in L1):
            las +=shu
        else:
            shu1.append(Decimal(las))
            shu1.append(shu)
            las = ''
    if las:  # 防崩
            shu1.append(Decimal(las))

    while '*' in shu1 or '/' in shu1:
        # 找第一个 * , / 的位置
        pos = 99999999999999999999
        for i in range(len(shu1)):
            if shu1[i] == '*' or shu1[i] == '/':
                pos = i
                break

        n1 = shu1[pos - 1]
        fu = shu1[pos]
        n2 = shu1[pos + 1]

        if fu == '*':
            result = n1 * n2
        elif fu == '/':
            if n2 == 0:
                messagebox.showerror('错误', 'WRONG')
                return
            result = n1 / n2

        shu1[pos - 1: pos + 2] = [result]

        #加减
    result = shu1[0]
    i = 1
    while i < len(shu1):
        fu = shu1[i]
        num = shu1[i + 1]
        if fu == '+':
            result += num
        else:
            result -= num
        i += 2

    display.delete(0, tk.END)
    display.insert(tk.END, str(result))
    fir.clear()
    fir.extend(list(str(result)))
    print(fir)









for hang, lie in enumerate(nums, start=1):
    for x, text in enumerate(lie):
        n = tk.Button(window,
                      text=text,
                      width=1,
                      height=1,
                      command = partial(press, text)
        )
        n.grid(row=hang, column=x,sticky='nsew', padx=2, pady=2)


for m, n in enumerate(cha, start=1):
    for x, text in enumerate(n):
        n = tk.Button(window2,
                      text=text,
                      width=1,
                      height=1,
                      command=partial(press, text)
        )
        n.grid(row=m, column=x,sticky='nsew', padx=2, pady=2)




window.rowconfigure(0, weight=60)
window.columnconfigure(0, weight=1)
for c in range(3):
    window.columnconfigure(c, weight=1)
for r in range(1, 5):
    window.rowconfigure(r, weight=15)


window2.rowconfigure(0, weight=0)
window2.columnconfigure(0, weight=1)

for q in range(1, 7):
    window2.rowconfigure(q, weight=1)

window2.columnconfigure(0, weight=1)
#学着写这些花了一个半小时。。。。。。。。

























window.mainloop()

