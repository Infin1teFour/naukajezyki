#Zaimportowanie bibliotek
import tkinter as tk
import random

# Inicjalizacja głównego okna Tkinter
root = tk.Tk()
root.title("Nauka - Trudne")
root.resizable(0, 0)

# Przygotowanie listy słówek i jej przetasowanie
wordlist = [("jabłko", "apple"), ("banan", "banana"), ("ogórek", "pickle")]
random.shuffle(wordlist)

# Inicjalizacja zmiennych
score = 0
current_polish, current_english = wordlist[score]

# Inicjalizacja zmiennej do śledzenia liczby błędnych odpowiedzi
loser = 0

# Funkcja zwracająca aktualne pytanie
def pytanie():
    return current_polish

# Inicjalizacja etykiet w głównym oknie
pytanie_L = tk.Label(root, text="", font=("Arial", 20), width=25, height=2)
pytanie_L.grid(row=0, column=0)

currentword = tk.Label(root, text=current_polish, font=("Arial", 20), width=25, height=2)
currentword.grid(row=1, column=0, columnspan=3)

scoredis = tk.Label(root, text="Punkty: " + str(score), font=("Arial", 20), width=25, height=2)
scoredis.grid(row=0, column=3)

# Pole do wprowadzania odpowiedzi
guess = tk.StringVar()
guess_entry = tk.Entry(root, width=20, font=("Arial", 20), textvariable=guess)
guess_entry.grid(row=2, column=0)

# Funkcja do sprawdzania odpowiedzi użytkownika
def check():
    global score, current_polish, current_english, wordlist, loser

    if score < len(wordlist):
        user_guess = guess.get()
        if user_guess:
            if user_guess == current_english:
                score += 1
                scoredis.config(text="Punkty: " + str(score))
                if score < len(wordlist):
                    current_polish, current_english = wordlist[score]
                    currentword.config(text=current_polish)
                    pytanie_L.config(text="")
                    guess.set("")
                else:
                    currentword.config(text="Gra zakończona")
            else:
                if loser == 3:
                    pytanie_L.config(text="Zła odpowiedź przegrałeś")
                    button.config(state="disabled")  # Wyłącz przycisk po przegranej
                else:
                    loser += 1
                    pytanie_L.config(text="Zła odpowiedź popełniłeś " + str(loser) + " błędy")

# Przycisk do sprawdzania odpowiedzi
button = tk.Button(root, text="Sprawdź", width=20, height=2, command=check)
button.grid(row=2, column=1)

# Uruchomienie głównej pętli Tkinter
check()
tk.mainloop()
