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
root.title("Nauka - Trudne")
root.resizable(0, 0)

# Inicjalizacja zmiennych
score = 0
current_finish =  ""

# Inicjalizacja zmiennej do śledzenia liczby błędnych odpowiedzi
loser = 0

# Funkcja do pobierania słówek z bazy danych
def get_wordlist_from_database():
    cursor = db.cursor()
    cursor.execute("SELECT napis_polski, fin_slowo FROM poziom3")
    return cursor.fetchall()

# Funkcja do losowania nowego słówka
def choose_random_word():
    global  current_finish
    current_finish = random.choice(wordlist)

# Przygotowanie listy słówek
wordlist = get_wordlist_from_database()
choose_random_word()