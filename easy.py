import tkinter as tk  # biblioteka tkinter  jako tk
from tkinter import messagebox  # messagebox z biblioteki tkinter
from PIL import ImageTk, Image  #  Image i ImageTk z biblioteki PIL (pillow)
import mysql.connector  # łącznik mysql
import random as r  # biblioteka random jako r
import matplotlib.pyplot as plt  # biblioteka matplotlib jako plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="trudnosci"
)



#okno 
root = tk.Tk()
root.title("nauka - poziom łatwy")
root.geometry("1200x800")
root.resizable("false", "false")
root.configure(bg="lightgrey")



def test():
    print('test')


#zmienne
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0



#przyciski
a1 = tk.Button(root, text="1", width=20, height=2, command= test)
a1.grid(row=4, column=0)

b1 = tk.Button(root, text="2", width=20, height=2, command= test)
b1.grid(row=4, column=1)

c1 = tk.Button(root, text="3", width=20, height=2, command= test)
c1.grid(row=4, column=2)

d1 = tk.Button(root, text="4", width=20, height=2, command= test)
d1.grid(row=5, column=0)

e1 = tk.Button(root, text="5", width=20, height=2, command= test)
e1.grid(row=5, column=1)

f1 = tk.Button(root, text="6", width=20, height=2, command= test)
f1.grid(row=5, column=2)







print("Poziom easy")
root.mainloop()