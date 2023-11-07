import tkinter as tk  # biblioteka tkinter  jako tk
from tkinter import messagebox  # messagebox z biblioteki tkinter
import mysql.connector  # łącznik mysql
import random as r  # biblioteka random jako r
from PIL import ImageTk, Image  # biblioteka pillow jako ImageTk, Image


#połączenie z bazą
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="trudnosci"
)

cursor = conn.cursor()
cursor.execute("SELECT napis, odpowiedz FROM poziom2")
result = cursor.fetchall()
r.shuffle(result)

#okno 
root = tk.Tk()
root.title("nauka - poziom średni")
root.resizable("false", "false")
root.configure(bg="lightgrey")

button1 = tk.Button(root, text="1", width=10, height=2, command=lambda: check(1))
button1.grid(row=1, column=0)
button2 = tk.Button(root, text="2", width=10, height=2, command=lambda: check(2))
button2.grid(row=1, column=1)
button3 = tk.Button(root, text="3", width=10, height=2, command=lambda: check(3))
button3.grid(row=1, column=2)
button4 = tk.Button(root, text="4", width=10, height=2, command=lambda: check(4))
button4.grid(row=1, column=3)
button5 = tk.Button(root, text="5", width=10, height=2, command=lambda: check(5))
button5.grid(row=2, column=0)
button6 = tk.Button(root, text="6", width=10, height=2, command=lambda: check(6))
button6.grid(row=2, column=1)
button7 = tk.Button(root, text="7", width=10, height=2, command=lambda: check(7))
button7.grid(row=2, column=2)
button8 = tk.Button(root, text="8", width=10, height=2, command=lambda: check(8))
button8.grid(row=2, column=3)

#słownik guzików
buttons = {
    1: button1,
    2: button2,
    3: button3,
    4: button4,
    5: button5,
    6: button6,
    7: button7,
    8: button8
}
nrPytanie = 0 
label = tk.Label(root)
label.grid(row=0, column=0, columnspan=4, pady=10, padx=10) 

def pytanie():
    try:
        for button in buttons.values():
            button.configure(bg="SystemButtonFace", state="normal")
        global img, label, nrPytanie, poprawne
        label.configure(text=result[nrPytanie][0])
        nrPytanie += 1
        poprawne = r.randint(1,8)
        lista = r.sample(result, 9)
        try:
            lista.remove(result[nrPytanie-1])
        except:
            pass
        for i in range(1,9):
            if i == poprawne:
                buttons[i].configure(text=result[nrPytanie-1][1])
            else:
                buttons[i].configure(text=lista[i-1][1])
    except IndexError:
        messagebox.showinfo("Koniec gry", "Gratulacje, udało Ci się ukończyć grę")
        root.destroy()

score = 0
scoreLabel = tk.Label(root, text="Punkty: " + str(score), font=("Arial", 20))
scoreLabel.grid(row=3, column=0, columnspan=4)

def check(odpowiedz):
    global poprawne, score
    if odpowiedz == poprawne:
        score += 1
        scoreLabel.configure(text="Punkty: " + str(score))
        pytanie()
    else:
        buttons[odpowiedz].configure(bg="red", state="disabled")


pytanie()
root.mainloop()