from tkinter import *
from tkinter.ttk import *

from time import strftime

root= Tk()
root.title("DataLoves Python Using  Digital Clock")

def time():
       string= strftime('%I : %M : %S %p %A ')
       Label.config(text=string)
       Label.after(1000,time)
Label=Label(root,font=("High Jersey Italic",80),background="black", foreground="cyan")
Label.pack(anchor="center")
time()
mainloop()
