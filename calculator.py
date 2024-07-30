from tkinter import *


def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def clear():
    e.delete(0, END)


def add():
    first_number = e.get()
    global f_num
    global operation
    f_num = int(first_number)
    operation = "addition"
    e.delete(0, END)


def equal():
    second_number = e.get()
    e.delete(0, END)
    
    match operation:
        case "addition":
            e.insert(0, f_num + int(second_number))
        case "subtraction":
            e.insert(0, f_num - int(second_number))
        case "multiplication":
            e.insert(0, f_num * int(second_number))
        case "division":
            e.insert(0, f_num / int(second_number))


def sub():
    first_number = e.get()
    global f_num
    global operation
    f_num = int(first_number)
    operation = "subtraction"
    e.delete(0, END)


def mul():
    first_number = e.get()
    global f_num
    global operation
    f_num = int(first_number)
    operation = "multiplication"
    e.delete(0, END)


def div():
    first_number = e.get()
    global f_num
    global operation
    f_num = int(first_number)
    operation = "division"
    e.delete(0, END)


root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=add)
button_clear = Button(root, text="Clear", padx=77, pady=20, command=clear)
button_equal = Button(root, text="=", padx=87, pady=20, command=equal)
button_sub = Button(root, text="-", padx=41, pady=20, command=sub)
button_mul = Button(root, text="*", padx=39, pady=20, command=mul)
button_div = Button(root, text="÷", padx=39, pady=20, command=div)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)

root.mainloop()