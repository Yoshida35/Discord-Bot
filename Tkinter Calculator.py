from tkinter import *
from tkinter import ttk

#https://docs.python.org/3/library/tkinter.html
#Python 3.10 looks ugly compared to python 3.9.

root = Tk()
frm = ttk.Frame(root, padding = 10)
frm.grid()

root.title("Calculator")

ttk.Button(frm, text = "Exit", command = root.destroy).grid(column = 0, row = 5)

#0-9
a = ttk.Button(frm, text = "0", ).grid(column = 1, row = 5)
b = ttk.Button(frm, text = "1").grid(column = 0, row = 2)
c = ttk.Button(frm, text = "2").grid(column = 1, row = 2)
d = ttk.Button(frm, text = "3").grid(column = 2, row = 2)
e = ttk.Button(frm, text = "4").grid(column = 0, row = 3)
f = ttk.Button(frm, text = "5").grid(column = 1, row = 3)
g = ttk.Button(frm, text = "6").grid(column = 2, row = 3)
h = ttk.Button(frm, text = "7").grid(column = 0, row = 4)
i = ttk.Button(frm, text = "8").grid(column = 1, row = 4)
j = ttk.Button(frm, text = "9").grid(column = 2, row = 4)

#operators
times = ttk.Button(frm, text = "x").grid(column = 3, row = 2)
divide = ttk.Button(frm, text = "/").grid(column = 3, row = 3)
add = ttk.Button(frm, text = "+").grid(column = 3, row = 4)
takeaway = ttk.Button(frm, text = "-").grid(column = 3, row = 5)
equals = ttk.Button(frm, text = "=").grid(column = 2, row = 5)


root.mainloop()
