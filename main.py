from tkinter import *
root = Tk()
root.title('Calculator')
root.iconbitmap('icon.ico')
root.geometry("361x381+500+200")

# functions
# for click


def click(number):
    global val
    val = val + str(number)
    var1.set(val)

# for clear


def clear():
    global val
    val = ""
    var1.set("")

# for equals


def equals():
    global val
    result = str(eval(val))
    var1.set(result)


# display
val = ""
var1 = StringVar()
e = Entry(root, bd=29, bg="black", fg="white", textvariable=var1, justify="right", font=('Ariel', 20))
e.grid(row=0, columnspan=4)

# first line
btn7 = Button(root, text="7", font=("Ariel", 12, "bold"), bg="powder blue", bd=12, height=2, width=6, command=lambda: click(7))
btn7.grid(row=1, column=0)
btn8 = Button(root, text="8", font=("Ariel", 12, "bold"), bg="powder blue", bd=12, height=2, width=6, command=lambda: click(8))
btn8.grid(row=1, column=1)
btn9 = Button(root, text="9", font=("Ariel", 12, "bold"), bg="powder blue", bd=12, height=2, width=6, command=lambda: click(9))
btn9.grid(row=1, column=2)
btn_clear = Button(root, text="C", bg="red", font=("Ariel", 12, "bold"), bd=12, height=2, width=6, command=clear)
btn_clear.grid(row=1, column=3)


# second line
btn4 = Button(root, text="4", font=("Ariel", 12, "bold"), bg="powder blue", bd=12, height=2, width=6, command=lambda: click(4))
btn4.grid(row=2, column=0)
btn5 = Button(root, text="5", font=("Ariel", 12, "bold"), bg="powder blue", bd=12, height=2, width=6, command=lambda: click(5))
btn5.grid(row=2, column=1)
btn6 = Button(root, text="6", font=("Ariel", 12, "bold"), bg="powder blue", bd=12, height=2, width=6, command=lambda: click(6))
btn6.grid(row=2, column=2)
btn_subtract = Button(root, text="_", font=("Ariel", 12, "bold"), bg="grey", bd=12, height=2, width=6, command=lambda: click("-"))
btn_subtract.grid(row=2, column=3)


# third line
btn1 = Button(root, text="1", font=("Ariel", 12, "bold"), bg="powder blue", bd=12, height=2, width=6, command=lambda: click(1))
btn1.grid(row=3, column=0)
btn2 = Button(root, text="2", font=("Ariel", 12, "bold"), bg="powder blue", bd=12, height=2, width=6, command=lambda: click(2))
btn2.grid(row=3, column=1)
btn3 = Button(root, text="3", font=("Ariel", 12, "bold"), bg="powder blue", bd=12, height=2, width=6, command=lambda: click(3))
btn3.grid(row=3, column=2)
btn_multi = Button(root, text="x", font=("Ariel", 12, "bold"), bg="grey", bd=12, height=2, width=6, command=lambda: click("*"))
btn_multi.grid(row=3, column=3)


# fourth line
btn_add = Button(root, text="+", font=("Ariel", 12, "bold"), bg="grey", bd=12, height=2, width=6, command=lambda: click("+"))
btn_add.grid(row=4, column=0)
btn0 = Button(root, text="0", font=("Ariel", 12, "bold"), bg="powder blue", bd=12, height=2, width=6, command=lambda: click(0))
btn0.grid(row=4, column=1)
btn_division = Button(root, text="÷", font=("Ariel", 12, "bold"), bg="grey", bd=12, height=2, width=6, command=lambda: click("/"))
btn_division.grid(row=4, column=2)
btn_equals = Button(root, text="=", font=("Ariel", 12, "bold"), bg="grey", bd=12, height=2, width=6, command=equals)
btn_equals.grid(row=4, column=3)


root.mainloop()
