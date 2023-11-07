import tkinter as tk
import mysql.connector
import random

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

# Funkcja zwracająca samogłoski z aktualnego pytania
def samogloski():
    return '_'.join([litera for litera in current_finnish if litera.lower() in vowels])

# Inicjalizacja etykiety wyświetlającej samogłoski
samogloski_L = tk.Label(root, text=samogloski(), font=("Arial", 20), width=25, height=2)
samogloski_L.grid(row=0, column=0)

currentword = current_finnish

scoredis = tk.Label(root, text="Punkty: " + str(score), font=("Arial", 20), width=25, height=2)
scoredis.grid(row=0, column=3)

# Pole do wprowadzania odpowiedzi
guess = tk.StringVar()
guess_entry = tk.Entry(root, width=20, font=("Arial", 20), textvariable=guess)
guess_entry.grid(row=2, column=0)

# Funkcja do sprawdzania odpowiedzi użytkownika
def check():
    global score, current_finnish, current_finish, wordlist, loser

    if score < len(wordlist):
        user_guess = guess.get()
        if user_guess:
            if user_guess == current_finnish:
                score += 1
                scoredis.config(text="Punkty: " + str(score))
                if score <= 20:
                    choose_random_word()
                    currentword = current_finnish
                    samogloski_L.config(text=samogloski())
                    guess.set("")
                else:
                    currentword = "Gra wygrałeś"
                    button.config(state="disabled")
            else:
                if loser == 3:
                    samogloski_L.config(text="Zła odpowiedź przegrałeś")
                    button.config(state="disabled")  # Wyłącz przycisk po przegranej
                else:
                    loser += 1
                    samogloski_L.config(text="Zła odpowiedź popełniłeś " + str(loser) + " błędy")

# Przycisk do sprawdzania odpowiedzi
button = tk.Button(root, text="Sprawdź", width=20, height=2, command=check)
button.grid(row=2, column=1)

# Uruchomienie głównej pętli Tkinter
check()
tk.mainloop()

# Zakończenie połączenia z bazą danych
db.close()
