from tkinter import *
from PIL import  ImageTk,Image

root = Tk()
root.title("Login interface")
root.minsize(100,100)
root.maxsize(600,600)
root.config(bg="skyblue")

img_label = Label(root,place=(12,10))
img = Image.open("OIP (1).jpg")


Image = ImageTk
root.mainloop()