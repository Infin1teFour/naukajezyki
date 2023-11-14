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
root.title("Nauka - Średnio / Trudne")
root.resizable(0, 0)
root.configure(bg="#dbdbd7")
vowels = {"a", "e", "i", "o", "u", "y", "-"}

# Inicjalizacja zmiennych
score = 0
current_finnish = ""

# Inicjalizacja zmiennej do śledzenia liczby błędnych odpowiedzi
loser = 0

# Funkcja do pobierania słówek z bazy danych
def get_wordlist_from_database():
    cursor = db.cursor()
    cursor.execute("SELECT fin_slowo FROM poziom3")
    return cursor.fetchall()

# Funkcja do losowania nowego słówka
def choose_random_word():
    global current_finnish
    current_finnish = random.choice(wordlist)
    current_finnish = str(current_finnish[0])  # Pobieramy pierwszy element z krotki

# Przygotowanie listy słówek
wordlist = get_wordlist_from_database()
choose_random_word()

# Funkcja do przekształcania słowa na formę do wyświetlenia
def display_word(word):
    displayed_word = ""
    for letter in word:
        if letter.lower() in vowels:
            displayed_word += letter
        else:
            displayed_word += " _ "
    return displayed_word

# Inicjalizacja etykiety wyświetlającej samogłoski jako litery, a współgłoski jako "_"
samogloski_L = tk.Label(root, text=display_word(current_finnish), font=("Arial", 20), width=25, height=2, bg="#dbdbd7")
samogloski_L.grid(row=0, column=0)

currentword = current_finnish

scoredis = tk.Label(root, text="Punkty: " + str(score), font=("Arial", 20), width=25, height=2, bg="#dbdbd7")
scoredis.grid(row=0, column=3)
loserdis = tk.Label(root, text="Błędy: " + str(loser), font=("Arial", 20), width=25, height=2, bg="#dbdbd7")
loserdis.grid(row=1, column=3)

# Pole do wprowadzania odpowiedzi
guess = tk.StringVar()
guess_entry = tk.Entry(root, width=20, font=("Arial", 20), textvariable=guess)
guess_entry.grid(row=2, column=0)

# Funkcja do sprawdzania odpowiedzi użytkownika
def check():
    global currentword, score, current_finnish, current_finish, wordlist, loser

    if score < len(wordlist):
        user_guess = guess.get()
        if user_guess:
            if user_guess == current_finnish:
                score += 1
                scoredis.config(text="Punkty: " + str(score))
                if score <= 20:
                    choose_random_word()
                    currentword = current_finnish
                    samogloski_L.config(text=display_word(current_finnish))
                    guess.set("")
                else:
                    currentword = "Gra wygrałeś"
                    button.config(state="disabled")
            else:
                if loser > 2 :
                    samogloski_L.config(text="Zła odpowiedź przegrałeś")
                    guess_entry.config(state="disabled")
                    button.config(state="disabled")  # Wyłącz przycisk po przegranej
                else:
                    loser =loser + 1
                    loserdis.config( text = "Błędy: "+ str(loser)  )
                    choose_random_word()
                    currentword = current_finnish
                    samogloski_L.config(text=display_word(current_finnish))
                    guess.set("")



# Przycisk do sprawdzania odpowiedzi
button = tk.Button(root, text="Sprawdź", width=20, height=2, command=check, bg= "#a6a6a2")
button.grid(row=2, column=1)

def wroc():
    root.destroy()
    os.system("python3 " + "nauka" + ".py") 
wroc_but = tk.Button(root, text="<--", width=10, height=2, command = wroc)
wroc_but.grid( row = 0 , column = 4 )       



# Uruchomienie głównej pętli Tkinter
root.mainloop()

# Zakończenie połączenia z bazą danych
db.close()
