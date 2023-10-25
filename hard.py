import tkinter as tk
import random

root = tk.Tk()
root.title("Nauka - Trudne")
root.resizable(0, 0)

wordlist = ["apple", "banana", "pickle"]
wordlist = random.sample(wordlist, 3)

display = wordlist
score = 0

currentword = tk.Label(root, text=display, font=("Arial", 20), width=25, height=2)
currentword.grid(row=0, column=0, columnspan=3)

scoredis = tk.Label(root, text="Punkty: " + str(score), font=("Arial", 20), width=25, height=2)
scoredis.grid(row=0, column=3)

guess = tk.StringVar()
guess_entry = tk.Entry(root, width=20, font=("Arial", 20), textvariable=guess)
guess_entry.grid(row=1, column=0)

def check():
    global display, score, wordlist
    if score < len(wordlist):
        correct = wordlist[score]
        display = ""
        if guess.get() == correct:
            score += 1
            scoredis.config(text="Punkty: " + str(score))
            if score < len(wordlist):
                display = "_ " * len(wordlist[score])
            currentword.config(text=display)
        else:
            display = ""
            for i in range(len(correct)):
                if i < len(guess.get()) and guess.get()[i] == correct[i]:
                    display += guess.get()[i]
                else:
                    display += "_ "
            currentword.config(text=display)

button = tk.Button(root, text="Sprawdź", width=20, height=2, command=check)
button.grid(row=1, column=1)

check()
tk.mainloop()
