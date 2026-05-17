import tkinter as tk
root = tk.Tk()
root.title("My first GUI APP")
root.geometry("400x300")

label = tk.Label(root,text = "Welcome to python GUI Programming")
label.pack()

root.mainloop()