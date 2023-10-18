import tkinter as tk

root = tk.Tk()
root.title("nauka - poziom łatwy")
root.geometry("1200x800")
root.resizable("false", "false")
root.configure(bg="lightgrey")






easy = tk.Button(root, text="łatwe", width=20, height=2)
easy.grid(row=4, column=0)

easy = tk.Button(root, text="łatwe", width=20, height=2)
easy.grid(row=4, column=1)

easy = tk.Button(root, text="łatwe", width=20, height=2)
easy.grid(row=4, column=2)

easy = tk.Button(root, text="łatwe", width=20, height=2)
easy.grid(row=5, column=0)

easy = tk.Button(root, text="łatwe", width=20, height=2)
easy.grid(row=5, column=1)

easy = tk.Button(root, text="łatwe", width=20, height=2)
easy.grid(row=5, column=2)








print("Poziom easy")
root.mainloop()