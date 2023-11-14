import tkinter as tk
import os

root = tk.Tk()
root.title("Nauka - beta v0.1")
root.geometry("600x200")
root.resizable(0, 0)
root.configure(bg="#dbdbd7")
def level(level):
    root.destroy()
    os.system("python3 " + level + ".py")

info = tk.Label(root, text="Witaj! Wybierz poziom trudności:", font=("Arial", 20, "bold"), width=25, height=2, bg="#dbdbd7")
info.grid(row=0, column=0, columnspan=3)

easy = tk.Button(root, text="łatwe", width=20, height=2, command=lambda: level("easy"), bg= "#a6a6a2", font=("Arial", 8,"bold"))
easy.grid(row=1, column=0)
easyinfo = tk.Label(root, text="Pokazuje się obrazek i \nwybierzasz spośród 6\n różnych odpowiedzi", font=("Arial", 10), width=18, height=3, bg="#dbdbd7", fg= "#4a4949")
easyinfo.grid(row=2, column=0)

medium = tk.Button(root, text="średnie", width=20, height=2, command=lambda: level("medium"), bg= "#a6a6a2", font=("Arial", 8,"bold"))
medium.grid(row=1, column=1)
mediuminfo = tk.Label(root, text="Przetłumacz słowo\n wybierając spośród\n 8 różnych odpowiedzi", font=("Arial", 10), width=18, height=3, bg="#dbdbd7", fg= "#4a4949")
mediuminfo.grid(row=2, column=1)

medhard = tk.Button(root, text="średnio-trudne", width=20, height=2, command=lambda: level("medhard"), bg= "#a6a6a2", font=("Arial", 8,"bold"))
medhard.grid(row=1, column=2)
medhardinfo = tk.Label(root, text="Wypełnij samogłoski\n w danym wyrazie", font=("Arial", 10), width=18, height=3, bg="#dbdbd7", fg= "#4a4949")
medhardinfo.grid(row=2, column=2)

hard = tk.Button(root, text="trudne", width=20, height=2, command=lambda: level("hard"), bg= "#a6a6a2", font=("Arial", 8,"bold"))
hard.grid(row=1, column=3)
medhardinfo = tk.Label(root, text="Przetłumacz słowo.\n Poprawne litery zostaną\n zaznaczone", font=("Arial", 10), width=18, height=3, bg="#dbdbd7", fg= "#4a4949")
medhardinfo.grid(row=2, column=3)

tk.mainloop()