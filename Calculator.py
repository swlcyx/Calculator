#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2023/11/8 9:25
# file: Calculator.py
# author: 孙伟亮
# email: 2849068933@qq.com
import tkinter as tk
from tkinter import messagebox


def ask_close():
    ask = messagebox.askokcancel('提示 ：', '你要退出计算器吗？')
    if ask == True:
        window.destroy()
        exit(0)


def display(x):
    t.insert('insert', str(x))
    equal()


def clear():
    t.delete('1.0', 'end')
    t_result.delete('1.0', 'end')


def dele():
    len1 = len(t.get('1.0', 'insert'))
    len2 = len1 - 1
    t.delete('1.' + str(len2), '1.' + str(len1))
    equal()


def equal():
    str1 = t.get('1.0', 'end')
    string = str1.replace('%', '/100').replace('x', '*')
    t_result.delete('1.0', 'end')
    try:
        num = round(eval(string), 8)
        t_result.insert('end', num)
    except:
        num = ''
        t_result.insert('end', num)


def equalall():
    str1 = t.get('1.0', 'end')
    string = str1.replace('%', '/100').replace('x', '*')
    t_result.delete('1.0', 'end')
    try:
        num = round(eval(string), 8)
        t.delete('1.0', 'end')
        t.insert('end', num)
    except:
        num = 'Wrong Expression!'
        t_result.insert('end', num)


if __name__ == '__main__':
    try:
        window = tk.Tk()
        window.title('孙伟亮的计算器')
        window.geometry('500x540')
        window.protocol('WM_DELETE_WINDOW', ask_close)
        window.resizable(width=False, height=False)
        tk.Label(window, bg='lavenderblush', width=100, height=100).place(x=0, y=0)

        # 第一排的按钮
        b_C = tk.Button(window, text='C', width=10, height=3, command=clear, font=('Arial', 12), bg='plum')
        b_C.place(x=50, y=140)
        b_division = tk.Button(window, text='/', width=10, height=3, command=lambda: display('/'), font=('Arial', 12),
                               bg='plum')
        b_division.place(x=152, y=140)
        b_multipy = tk.Button(window, text='x', width=10, height=3, command=lambda: display('x'), font=('Arial', 12),
                              bg='plum')
        b_multipy.place(x=254, y=140)
        b_delete = tk.Button(window, text='<=', width=10, height=3, command=dele, font=('Arial', 12), bg='plum')
        b_delete.place(x=356, y=140)

        # 第二排的按钮
        b_7 = tk.Button(window, text='7', width=10, height=3, command=lambda: display('7'), font=('Arial', 12),
                        bg='lavender')
        b_7.place(x=50, y=210)
        b_8 = tk.Button(window, text='8', width=10, height=3, command=lambda: display('8'), font=('Arial', 12),
                        bg='lavender')
        b_8.place(x=152, y=210)
        b_9 = tk.Button(window, text='9', width=10, height=3, command=lambda: display('9'), font=('Arial', 12),
                        bg='lavender')
        b_9.place(x=254, y=210)
        b_subtraction = tk.Button(window, text='--', width=10, height=3, command=lambda: display('-'),
                                  font=('Arial', 12), bg='plum')
        b_subtraction.place(x=356, y=210)

        # 第三排的按钮
        b_4 = tk.Button(window, text='4', width=10, height=3, command=lambda: display('4'), font=('Arial', 12),
                        bg='lavender')
        b_4.place(x=50, y=280)
        b_5 = tk.Button(window, text='5', width=10, height=3, command=lambda: display('5'), font=('Arial', 12),
                        bg='lavender')
        b_5.place(x=152, y=280)
        b_6 = tk.Button(window, text='6', width=10, height=3, command=lambda: display('6'), font=('Arial', 12),
                        bg='lavender')
        b_6.place(x=254, y=280)
        b_addition = tk.Button(window, text='+', width=10, height=3, command=lambda: display('+'), font=('Arial', 12),
                               bg='plum')
        b_addition.place(x=356, y=280)

        # 第四排的按钮
        b_1 = tk.Button(window, text='1', width=10, height=3, command=lambda: display('1'), font=('Arial', 12),
                        bg='lavender')
        b_1.place(x=50, y=350)
        b_2 = tk.Button(window, text='2', width=10, height=3, command=lambda: display('2'), font=('Arial', 12),
                        bg='lavender')
        b_2.place(x=152, y=350)
        b_3 = tk.Button(window, text='3', width=10, height=3, command=lambda: display('3'), font=('Arial', 12),
                        bg='lavender')
        b_3.place(x=254, y=350)
        b_equalall = tk.Button(window, text='=', width=10, height=7, command=equalall, font=('Arial', 12),
                               bg='blueviolet')
        b_equalall.place(x=356, y=348)

        # 第五排的按钮
        b_percent = tk.Button(window, text='%', width=10, height=3, command=lambda: display('%'), font=('Arial', 12),
                              bg='lavender')
        b_percent.place(x=50, y=420)
        b_0 = tk.Button(window, text='0', width=10, height=3, command=lambda: display('0'), font=('Arial', 12),
                        bg='lavender')
        b_0.place(x=152, y=420)
        b_spot = tk.Button(window, text='.', width=10, height=3, command=lambda: display('.'), font=('Arial', 12),
                           bg='lavender')
        b_spot.place(x=254, y=420)

        # 显示栏
        t = tk.Text(window, height=1, width=24, font=('Arial', 24))
        t.place(x=35, y=30)
        t_result = tk.Text(window, height=1, width=24, font=('Arial', 24))
        t_result.place(x=35, y=72)

        window.mainloop()
    except SystemExit:
        pass
