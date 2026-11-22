# Import everything from tkinter module
from tkinter import *

# Create a tkinter window
root = Tk()

# Open window having dimension 100x100
root.geometry('500x500')

# Create a Button
btn = Button(root, text='Click me !', bd='5',
             background="cyan")

# Set the position of button on the top of window.
# Try side = bottom, right, left

btn.pack(side='right')

root.mainloop()