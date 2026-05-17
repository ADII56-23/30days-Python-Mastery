from tkinter import *
#open window
root = Tk()
root.title("Basic Signin")
root.minsize(200,400)
root.maxsize(800,800 )
root.geometry("400x400")

label=Label(root,text="welcome back!! ",bg="light blue")
label.grid(row=0, column=0 )


Label(root,text="First name").grid(row=1,column=0)
Label(root,text="Last name").grid(row=2,column=0)

entry1 = Entry(root)
entry2 = Entry(root)
entry1.grid(row=1,column=1)
entry2.grid(row=2,column=1)

Label(root,text="Gender").grid(row=3)
gender = IntVar()
Checkbutton(root,text="Male", variable=gender).grid(row=3,column=1,sticky=W)
Checkbutton(root,text="female",variable=gender).grid(row=4,column=1,sticky=W)

age = StringVar()
Radiobutton(root, text="Are you 18+",variable=age,value="yes").grid(row=5,column=0,sticky=W)
Radiobutton(root,text="No,i'm not",variable=age,value="no").grid(row=5,column=1,sticky=W)




button = Button(root, text="stop" , width=25,command=root.destroy)
button.grid(row=7, column=0)

#mainloop() open the window for the user to perform tasks
root.mainloop()