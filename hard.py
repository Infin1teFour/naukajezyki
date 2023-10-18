import tkinter as tk
import os
import random

root = tk.Tk()
root.title("Nauka - Trudne")
root.resizable(0, 0)

wordlist = ["apple", "banana", "pickle"]
wordlist = random.sample(wordlist, 3)

display = ""
guess = tk.StringVar()
score = 0

currentword = tk.Label(root, text=display, font=("Arial", 20), width=25, height=2)
currentword.grid(row=0, column=0, columnspan=3)

scoredis = tk.Label(root, text="Punkty: " + str(score), font=("Arial", 20), width=25, height=2)
scoredis.grid(row=0, column=3)

guess = tk.Entry(root, width=20, font=("Arial", 20), textvariable=guess)
guess.grid(row=1, column=0)

def check():
    global display, score, wordlist
    correct = wordlist[score]
    display = ""
    if guess.get() == correct:
        score += 1
        scoredis.config(text="Punkty: " + str(score))
        for letter in wordlist[score]:
            display = "_ "
        currentword.config(text=display)
    else:
        i = 0
        for letter in correct:
            if letter == guess[i]:
                display += letter
            else:
                display += "_ "
            i += 1
        currentword.config(text=display)

button = tk.Button(root, text="Sprawdź", width=20, height=2, command=check)
button.grid(row=1, column=1)

check()
tk.mainloop()