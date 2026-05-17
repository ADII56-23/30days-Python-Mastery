import tkinter as tk
from tkinter import messagebox

def register():
    name = name_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    confirm = confirm_entry.get()

    if name == "" or email == "" or password == "" or confirm == "":
        messagebox.showerror("Error", "Please fill all fields")
    elif password != confirm:
        messagebox.showerror("Error", "Passwords do not match")
    else:
        messagebox.showinfo("Success", "Registration Successful")

root = tk.Tk()
root.title("Registration Form")
root.geometry("400x400")
root.configure(bg="lightblue")


title = tk.Label(root, text="Registration Form", font=("Arial", 18, "bold"), bg="lightblue", fg="darkblue")
title.pack(pady=10)


tk.Label(root, text="Name", bg="lightblue", font=("Arial", 12)).pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)


tk.Label(root, text="Email", bg="lightblue", font=("Arial", 12)).pack()
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)


tk.Label(root, text="Password", bg="lightblue", font=("Arial", 12)).pack()
pass_entry = tk.Entry(root, show="*", width=30)
pass_entry.pack(pady=5)


tk.Label(root, text="Confirm Password", bg="lightblue", font=("Arial", 12)).pack()
confirm_entry = tk.Entry(root, show="*", width=30)
confirm_entry.pack(pady=5)


register_btn = tk.Button(root, text="Register", bg="green", fg="white", width=15, command=register)
register_btn.pack(pady=20)

root.mainloop()