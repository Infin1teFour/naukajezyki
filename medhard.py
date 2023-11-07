import tkinter as tk

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="trudnosci"
)

cursor = conn.cursor()
cursor.execute("SELECT napis, odpowiedz FROM poziom2")
result = cursor.fetchall()
r.shuffle(result)

root = tk.Tk()
root.title("nauka - poziom Średnnio-Trudny")
root.geometry("1200x800")
root.resizable("false", "false")

