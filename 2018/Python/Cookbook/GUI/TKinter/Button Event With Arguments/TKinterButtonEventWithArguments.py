from tkinter import *

def button_call(color_in):
    print("hey you pressed the {} button".format(color_in))

root = Tk()
frame = Frame(root)
frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

red_button = Button(frame, text="Red", fg="red", command= lambda: button_call("red"))
red_button.pack(side=LEFT)

green_button = Button(frame, text="Brown", fg="brown", command=lambda: button_call("green"))
green_button.pack(side=LEFT)

blue_button = Button(frame, text="Blue", fg="blue", command=lambda: button_call("blue"))
blue_button.pack(side=LEFT)

black_button = Button(bottom_frame, text="Black", fg="black", command=lambda: button_call("black"))
black_button.pack(side=BOTTOM)

root.mainloop()
