import mysql.connector
from tkinter import *

# enter a string into the empty field at the top right of the corner,
# then press "click me", this will display the text in the canvas

r = Tk()

# get entry input and update the text in canvas
def Container_Text_Update():
    Text = Input.get()
    Info.itemconfigure(Info_Text, text=Text)


Info = Canvas(r, width=400, height=400, bg="white")
Info.create_text(200,10, text="Info Box")
# The below text is set by the Container_text_Update function
# anchor="nw" means that the text starts from top left
# width=380 means that, that's the maximum lenght of text before it's warped
Info_Text = Info.create_text(15,20, anchor="nw", width=380)


Input = Entry(r, width=100)


GetIt=Button(r, text="Click Me", command=Container_Text_Update)

# Layout
Info.pack(side=LEFT, fill=Y)
Input.pack(side=TOP)
GetIt.pack(side=TOP)
    
r.geometry("700x500")


