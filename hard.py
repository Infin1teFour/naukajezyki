import tkinter as tk
import random

root = tk.Tk()
root.title("Nauka - Trudne")
root.resizable(0, 0)

wordlist = [("jabłko", "apple"), ("banan", "banana"), ("ogórek", "pickle")]
random.shuffle(wordlist)

score = 0
current_polish, current_english = wordlist[score]

def pytanie():
    return current_polish

pytanie_L = tk.Label(root, text="", font=("Arial", 20), width=25, height=2)
pytanie_L.grid(row=0, column=0, columnspan=3)

currentword = tk.Label(root, text=current_polish, font=("Arial", 20), width=25, height=2)
currentword.grid(row=1, column=0, columnspan=3)

scoredis = tk.Label(root, text="Punkty: " + str(score), font=("Arial", 20), width=25, height=2)
scoredis.grid(row=0, column=3)

guess = tk.StringVar()
guess_entry = tk.Entry(root, width=20, font=("Arial", 20), textvariable=guess)
guess_entry.grid(row=2, column=0)

def check():
    global score, current_polish, current_english, wordlist
    if score < len(wordlist):
        if guess.get() == current_english:
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
            pytanie_L.config(text="Zła odpowiedź")

button = tk.Button(root, text="Sprawdź", width=20, height=2, command=check)
button.grid(row=2, column=1)

check()
tk.mainloop()
