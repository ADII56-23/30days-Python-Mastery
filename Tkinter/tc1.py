import tkinter as tk
root = tk.Tk()
root.geometry("400x300")

tk.Label(root, text="enter your name").grid(row=0, column=0, padx = 10, pady =10)
entry = tk.Entry(root)
entry.grid(row=0, column=1,padx = 10, pady=10)

def on_click():
  print("Hello students! welcome to Tkinter")

button = tk.Button(root,text="click me", command=on_click)
button.grid(row=2, column=0)

root.mainloop()