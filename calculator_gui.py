#Calculator App

import tkinter as tk
import tkinter.ttk as ttk
import math

app = tk.Tk()
app.title("Calculator")

answer = tk.IntVar(app, value=0)
operation=""


def update_result(i):
    result.set(i)

def clear():
    result.set(0)

def add():
    answer.set(result.get())
    result.set(0)
    global operation 
    operation = "+"

def times():
    answer.set(result.get())
    result.set(0)
    global operation 
    operation = "*"

def minus():
    answer.set(result.get())
    result.set(0)
    global operation 
    operation = "-"

def sin_button_function():
    x = result.get()
    y = math.sin(x)
    result.set(y)

def cos_button_function():
    x = result.get()
    y = math.cos(x)
    result.set(y)

def asin_button_function():
    try:
        x = result.get()
        y = math.asin(x)
        result.set(y)
    except:
        result.set("NAN")

def acos_button_function():
    try:
        x = result.get()
        y = math.acos(x)
        result.set(y)
    except:
        result.set("NAN")



def equals():
    global operation
    if operation == "+":
        result.set(answer.get() + result.get())
        operation = ""
    elif operation =="*":
        result.set(answer.get() * result.get())
        operation = ""
    elif operation == "-":
        result.set(answer.get() - result.get())
        operation = ""



#result
result = tk.IntVar(app, value = 0)
result_label = ttk.Label(app, width = 30, textvariable = result)
result_label.grid(row=0, column=0, columnspan=3)



#number buttons
buttons = [ttk.Button(app, width = 10, text= i, command = lambda x = i: update_result(x)) for i in range(10)]
for i in range(10):
    buttons[i].grid(row = 1 + (i//3), column = i%3)

add_button=ttk.Button(app, width=10, text="+", command = add)
add_button.grid(row= 1, column=3)

substract_button=ttk.Button(app, width=10, text="-", command = minus)
substract_button.grid(row= 2, column=3)

times_button=ttk.Button(app, width=10, text="*", command = times)
times_button.grid(row= 3, column=3)

equals_button=ttk.Button(app, width=10, text="=", command = equals)
equals_button.grid(row= 4, column=3)

clear_button=ttk.Button(app, width=10, text="c", command = clear)
clear_button.grid(row= 4, column=2)

sin_button=ttk.Button(app, width=10, text="sin", command = sin_button_function)
sin_button.grid(row= 1, column=4)

cos_button=ttk.Button(app, width=10, text="cos", command = cos_button_function)
cos_button.grid(row= 2, column=4)

asin_button=ttk.Button(app, width=10, text="arcsin", command = asin_button_function)
asin_button.grid(row= 3, column=4)

acos_button=ttk.Button(app, width=10, text="arccos", command = acos_button_function)
acos_button.grid(row= 4, column=4)



app.mainloop()
