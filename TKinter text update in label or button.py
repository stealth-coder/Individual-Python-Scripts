from tkinter import *

r = Tk()

# this functions changes the button's text
def update_text():
    btn_text.set("Updated")


btn_text = StringVar()

# the command is activated when the user clicks the button 
My_Button = Button(r, textvariable=btn_text, command=update_text).pack()

# buttons text when the program is started
btn_text.set("Not updated")

r.geometry("300x300")

r.mainloop()
