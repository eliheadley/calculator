# Purpose: Improve Python skills by making a calculator
# By:      Eli Headley - 12/11/2023

from calc import *
import tkinter as tk

# input from calculator
expression = ""

# create functions for typind on calculator
def add_to_expression(symbol):
    global expression
    expression += str(symbol)
    text_field.delete(1.0, "end")
    text_field.insert(1.0, expression)

def eval_expression():
    global expression
    try:
        expression = str(eval(expression))
        text_field.delete(1.0, "end")
        text_field.insert(1.0, expression)
    except:
        clear_field()
        text_field.insert(1.0, "Error")

def clear_field():
    global expression
    expression = ""
    text_field.delete(1.0, "end")


# create framwork for calculator
root = tk.Tk()

root.geometry("300x275")
text_field = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_field.grid(columnspan=5)

# All digit buttons
btn_1 = tk.Button(root, text="1", command=lambda: add_to_expression(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_expression(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_expression(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_expression(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_expression(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_expression(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_expression(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_expression(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_expression(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_expression(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)
btn_par1 = tk.Button(root, text="(", command=lambda: add_to_expression('('), width=5, font=("Arial", 14))
btn_par1.grid(row=5, column=1)
btn_par2 = tk.Button(root, text=")", command=lambda: add_to_expression(')'), width=5, font=("Arial", 14))
btn_par2.grid(row=5, column=3)

# clear and evaluate button
btn_clr = tk.Button(root, text="C", command=clear_field, width=11, font=("Arial", 14))
btn_clr.grid(row=6, column=1, columnspan=2)
btn_eval = tk.Button(root, text="=", command=eval_expression, width=11, font=("Arial", 14))
btn_eval.grid(row=6, column=3, columnspan=2)

# operation buttons
btn_add = tk.Button(root, text="+", command=lambda: add_to_expression("+"), width=5, font=("Arial", 14))
btn_add.grid(row=2, column=4)
btn_sub = tk.Button(root, text="-", command=lambda: add_to_expression("-"), width=5, font=("Arial", 14))
btn_sub.grid(row=3, column=4)
btn_mult = tk.Button(root, text="*", command=lambda: add_to_expression("*"), width=5, font=("Arial", 14))
btn_mult.grid(row=4, column=4)
btn_div = tk.Button(root, text="/", command=lambda: add_to_expression("/"), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=4)


root.mainloop()