from tkinter import *

def button_call():
    print("hey you pressed a button")

root = Tk()
frame = Frame(root)
frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

red_button = Button(frame, text="Red", fg="red", command=button_call)
red_button.pack(side=LEFT)

green_button = Button(frame, text="Brown", fg="brown", command=button_call)
green_button.pack(side=LEFT)

blue_button = Button(frame, text="Blue", fg="blue", command=button_call)
blue_button.pack(side=LEFT)

black_button = Button(bottom_frame, text="Black", fg="black", command=button_call)
black_button.pack(side=BOTTOM)

root.mainloop()
