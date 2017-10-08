from tkinter import *
"""
To initialise Tkinter we have to create a Tk root widget. The root widget is a window with a title-bar
and a window manager.

Next we create a label. A Label is certain type of widget that allows us to, among other things, write on it.

The pack method tells Tk to fit the size of the window to the given text.

The window won't appear until we tell Tkinter's main loop to start looping.
"""

root = Tk()
w = Label(root, text="Hello World!")

w.pack()
root.mainloop()
