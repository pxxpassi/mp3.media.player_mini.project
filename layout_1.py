# Import module
from tkinter import *
import pygame

# Creating object 
root = Tk()
root.title("SMASH MUSIC - MP3 PLAYER")
text = Text(root,height = 40, width = 20, font=("Calibri", 15))
x = "MUSIC PLAYER"
text.insert(END,x)

# Adjusting size 
root.geometry("850x500")
# Adding image file
bg = PhotoImage(file = "bg.png")
  
# Create Canvas
canvas1 = Canvas( root, width = 1,
                 height = 500)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "n")
  
listbox = Listbox(root, width = 50 , height = 10, bg = "light blue", fg = "black")

# Create Buttons
button1 = Button( root, text = "  ▶  ", font=("Calibri",11))
button2 = Button( root, text = " ⏸ ", font=("Calibri",11))
button3 = Button( root, text = "REPLAY", font=("Calibri",9))
button4 = Button( root, text = "  ⏭  ", font=("Calibri",12))
button5 = Button( root, text = "  ⏮  ", font=("Calibri",12))
button6= Button( root, text = "EXIT", font=("Calibri",11))


# Display Buttons
button1_canvas = canvas1.create_window( 400, 240, 
                                       anchor = "nw",
                                       window = button1)#play button
  
button2_canvas = canvas1.create_window( 400, 290,
                                       anchor = "nw",
                                       window = button2)#pause button
button3_canvas = canvas1.create_window( 397, 339,
                                        anchor = "nw",
                                       window = button3)#replay button

button4_canvas = canvas1.create_window( 500, 240, 
                                       anchor = "nw",
                                       window = button4)#next button

button5_canvas = canvas1.create_window( 300, 240, 
                                       anchor = "nw",
                                       window = button5)#previous button

button6_canvas = canvas1.create_window( 700, 430, 
                                       anchor = "nw",
                                       window = button6)# exit button

listbox_canvas = canvas1.create_window(270,50, anchor = "nw",
                                       window = listbox)

text_canvas = canvas1.create_window(270,20,anchor = "nw", window = text)

root.mainloop()
