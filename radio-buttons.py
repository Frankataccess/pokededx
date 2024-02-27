 
# Importing Tkinter module
from tkinter import *
import time
# from tkinter.ttk import *
 
# Creating master Tkinter window
master = Tk()
master.geometry("175x175")
 
# Tkinter string variable
# able to store any string value
v = StringVar(master, "0")
 
# Dictionary to create multiple buttons
values = {"Pokemon 1" : "1",
          "My Team 2" : "2",
          "Account 3" : "3",
          "Exit Program" : "4"
          }
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(master, text = text, variable = v, 
                value = value, indicator = 0,
                background = "light blue").pack(ipady = 5)
                 
 
# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())
mainloop()