import tkinter as tk
from tkinter import *
import random
import string

pas = ""

def Gen_pass():
    global pas
    try:
        if entry_1.get() and entry_2.get():
            le = int(entry_2.get())
            l = string.ascii_letters + string.digits + string.punctuation
            pas = ''.join(random.choice(l) for i in range(le))
            pas1 = "The Password Generated is :  "+pas
            label_3.config(text=pas1,fg='red')
        elif entry_2.get():
            pas = "Enter User Name !!"
            label_3.config(text=pas,fg='red')
        else:
            pas = "Enter Desired length of password !!"
            label_3.config(text=pas,fg='red')            
    except ValueError:
        print("Please enter a valid integer for the password length.")
        
def Reset_pass():
    entry_1.delete(0,END)
    entry_2.delete(0,END)
    label_3.config(text="")
    label_4.config(text="")

def Accept_pass():
    global pas
    s = "Hello "+entry_1.get()+"! your password is :  "+pas
    label_4.config(text=s)

window = tk.Tk()
window.geometry('500x500')
window.configure(bg='pink')

label_1 = tk.Label(window,text="PASSWORD GENERATOR",font=("Times New Roman",40,"bold"),fg="black",bg='pink')
label_1.place(x=450,y=4)

label_2 = tk.Label(window,text="Enter  User  Name  : ",font=("Times New Roman",25),fg="black",bg='pink')
label_2.place(x=350,y=150)

entry_1 = tk.Entry(window,font=('Times New Roman',23))
entry_1.place(x=680,y=155)

label_2 = tk.Label(window,text= "Enter  the  desired  length  of  the  password  :",font=("Times New Roman",25),bg='pink')
label_2.place(x=200,y=250)
    
entry_2 = tk.Entry(window,font=('Times New Roman',20))
entry_2.place(x=930,y=260)

button_1 = tk.Button(window,text="Generate_Password",font=('Times New Roman',20,"bold"),bg='cyan',command=Gen_pass)
button_1.place(x=300,y=400)

button_2 = tk.Button(window,text="Accept_Password",font=('Times New Roman',20,"bold"),bg='lavender',command=Accept_pass)
button_2.place(x=640,y=400)

button_3 = tk.Button(window,text=" Reset_Password ",font=('Times New Roman',20,"bold"),bg='yellow',command=Reset_pass)
button_3.place(x=950,y=400)

label_3 = tk.Label(window,font=("Times New Roman",25,"bold"),bg='pink')
label_3.place(x=300,y=550)

label_4 = tk.Label(window,font=("Times New Roman",25,"bold"),bg='pink')
label_4.place(x=300,y=650)

window.mainloop()
