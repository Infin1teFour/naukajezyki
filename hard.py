import tkinter as tk
import mysql.connector
import random
import os

# Połączenie z bazą danych MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="trudnosci"
)

# Inicjalizacja głównego okna Tkinter
root = tk.Tk()
root.title("Nauka - Trudne")
root.resizable(0, 0)
root.configure(bg="#dbdbd7")
# Inicjalizacja zmiennych
score = 0
current_polish, current_finish = "", ""

# Inicjalizacja zmiennej do śledzenia liczby błędnych odpowiedzi
loser = 0

# Funkcja do pobierania słówek z bazy danych
def get_wordlist_from_database():
    cursor = db.cursor()
    cursor.execute("SELECT napis_polski, fin_slowo FROM poziom3")
    return cursor.fetchall()

# Funkcja do losowania nowego słówka
def choose_random_word():
    global current_polish, current_finish
    current_polish, current_finish = random.choice(wordlist)

# Przygotowanie listy słówek
wordlist = get_wordlist_from_database()
choose_random_word()

# Funkcja zwracająca aktualne pytanie
def pytanie():
    return current_polish

# Inicjalizacja etykiet w głównym oknie
pytanie_L = tk.Label(root, text="", font=("Arial", 20), width=25, height=2, bg="#dbdbd7")
pytanie_L.grid(row=0, column=0)

currentword = tk.Label(root, text=current_polish, font=("Arial", 20), width=25, height=2, bg="#dbdbd7")
currentword.grid(row=1, column=0, columnspan=3)

scoredis = tk.Label(root, text="Punkty: " + str(score), font=("Arial", 20), width=25, height=2, bg="#dbdbd7")
scoredis.grid(row=0, column=3)

# Pole do wprowadzania odpowiedzi
guess = tk.StringVar()
guess_entry = tk.Entry(root, width=20, font=("Arial", 20), textvariable=guess)
guess_entry.grid(row=2, column=0)

# Funkcja do sprawdzania odpowiedzi użytkownika
def check():
    global score, current_polish, current_finish, wordlist, loser

    if score < len(wordlist):
        user_guess = guess.get()
        if user_guess:
            if user_guess == current_finish:
                score += 1
                scoredis.config(text="Punkty: " + str(score))
                if score <= 20:
                    choose_random_word()
                    currentword.config(text=current_polish)
                    pytanie_L.config(text="")
                    guess.set("")
                else:
                    currentword.config(text="Gra wygrałeś")
                    button.config(state="disabled")
                    guess.set("")
            else:
                if loser == 2:
                    pytanie_L.config(text="Zła odpowiedź przegrałeś")
                    button.config(state="disabled")  # Wyłącz przycisk po przegranej
                    guess.set("")
                    guess_entry.config( state= "disabled")
                else:
                    loser += 1
                    pytanie_L.config(text="Zła odpowiedź popełniłeś " + str(loser) + " błędy")
                    guess.set("")

# Przycisk do sprawdzania odpowiedzi
button = tk.Button(root, text="Sprawdź", width=20, height=2, command=check, bg= "#a6a6a2")
button.grid(row=2, column=1)
#Przycisk do powrotu do mmenu głównego
def wroc():
    root.destroy()
    os.system("python3 " + "nauka" + ".py") 
wroc_but = tk.Button(root, text="<--", width=10, height=2, command = wroc, bg= "#3b3b38", fg="white")
wroc_but.grid( row = 0 , column = 5 )       



# Uruchomienie głównej pętli Tkinter
check()
tk.mainloop()

# Zakończenie połączenia z bazą danych
db.close()
