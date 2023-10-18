import tkinter as tk

root = tk.Tk()
root.title("nauka - poziom łatwy")
root.geometry("1200x800")
root.resizable("false", "false")
root.configure(bg="lightgrey")


def test():
    print('test')



easy = tk.Button(root, text="1", width=20, height=2, command= test)
easy.grid(row=4, column=0)

easy = tk.Button(root, text="2", width=20, height=2, command= test)
easy.grid(row=4, column=1)

easy = tk.Button(root, text="3", width=20, height=2, command= test)
easy.grid(row=4, column=2)

easy = tk.Button(root, text="4", width=20, height=2, command= test)
easy.grid(row=5, column=0)

easy = tk.Button(root, text="5", width=20, height=2, command= test)
easy.grid(row=5, column=1)

easy = tk.Button(root, text="6", width=20, height=2, command= test)
easy.grid(row=5, column=2)








print("Poziom easy")
root.mainloop()