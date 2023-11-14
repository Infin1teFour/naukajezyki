import tkinter as tk  # biblioteka tkinter  jako tk
from tkinter import messagebox  # messagebox z biblioteki tkinter
import mysql.connector  # łącznik mysql
import random as r  # biblioteka random jako r
from PIL import ImageTk, Image  # biblioteka pillow jako ImageTk, Image
import os


#połączenie z bazą
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="trudnosci"
)
loser = 0

cursor = conn.cursor()
cursor.execute("SELECT napis, odpowiedz FROM poziom1")
result = cursor.fetchall()
r.shuffle(result)

#okno 
root = tk.Tk()
root.title("nauka - poziom łatwy")
root.resizable("false", "false")
root.configure(bg="#dbdbd7")

button1 = tk.Button(root, text="1", width=10, height=2, command=lambda: check(1), bg= "#a6a6a2")
button1.grid(row=1, column=0)
button2 = tk.Button(root, text="2", width=10, height=2, command=lambda: check(2), bg= "#a6a6a2")
button2.grid(row=1, column=1)
button3 = tk.Button(root, text="3", width=10, height=2, command=lambda: check(3), bg= "#a6a6a2")
button3.grid(row=1, column=2)
button4 = tk.Button(root, text="4", width=10, height=2, command=lambda: check(4), bg= "#a6a6a2")
button4.grid(row=2, column=0)
button5 = tk.Button(root, text="5", width=10, height=2, command=lambda: check(5), bg= "#a6a6a2")
button5.grid(row=2, column=1)
button6 = tk.Button(root, text="6", width=10, height=2, command=lambda: check(6), bg= "#a6a6a2")
button6.grid(row=2, column=2)

#słownik guzików
buttons = {
    1: button1,
    2: button2,
    3: button3,
    4: button4,
    5: button5,
    6: button6
}
nrPytanie = 0 
label = tk.Label(root)
label.grid(row=0, column=0, columnspan=3)

def pytanie():
    try:
        for button in buttons.values():
            button.configure(bg="#a6a6a2", state="normal")
        global img, label, nrPytanie, poprawne
        currentImage = "grafika/"+result[nrPytanie][0]+".png"
        img = ImageTk.PhotoImage(Image.open(currentImage))
        label.configure(image=img)
        nrPytanie += 1
        poprawne = r.randint(1,6)
        lista = r.sample(result, 7)
        try:
            lista.remove(result[nrPytanie-1])
        except:
            pass
        for i in range(1,7):
            if i == poprawne:
                buttons[i].configure(text=result[nrPytanie-1][1])
            else:
                buttons[i].configure(text=lista[i-1][1])
    except IndexError:
        messagebox.showinfo("Koniec gry", "Gratulacje, udało Ci się ukończyć grę")
        root.destroy()

score = 0
scoreLabel = tk.Label(root, text="Punkty: " + str(score), font=("Arial", 20), bg="#dbdbd7")
scoreLabel.grid(row=3, column=0, columnspan=3)

def check(odpowiedz):
    global poprawne, score, loser
    if odpowiedz == poprawne:
        score += 1
        scoreLabel.configure(text="Punkty: " + str(score))
        pytanie()
    else:
        buttons[odpowiedz].configure(bg="red", state="disabled")
        loser += 1
        if loser == 6:
            messagebox.showerror("Koniec gry", "Przegrałeś")
            root.destroy()

def wroc():
    root.destroy()
    os.system("python3 " + "nauka" + ".py") 
wroc_but = tk.Button(root, text="<--", width=5, height=1, command = wroc, bg= "#3b3b38", fg="white")
wroc_but.grid( row = 4 , column = 0 )       




pytanie()
root.mainloop()