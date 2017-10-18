from tkinter import *  # we are going to import everything in TKinter for simplicity


# Let's make a blueprint that represents our window.
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()              # after we have set up the super amd self, init the window

    def init_window(self):
        """
        Init window initialises the basic window.
        It does this by completing four tasks:
        1. Setting the title
        2. Defining how the window behaves if you move or expand it or if
                you introduce an element that is larger than the window
                currently is.
        3. Creates a button
        4. Places that button on the x,y coordinate
        """
        self.master.title("Hello world!")
        self.pack(fill=BOTH, expand=1)

        """
        Creates a quit button that can call a method. 
        """
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=0, y=0)



    def client_exit(self):
        """
        A method that is run when the quit button is pressed
        """
        print("THAT'S IT, I'M TAKING MY BAT AND BALL AND I AM GOING HOME!")
        exit()


root = Tk()                             # Tk() is a top level widget of Tk. We got it from the import
root.geometry("400x300")                # We're going to define how big this window is
app = Window(root)                      # Window needs a root object (Tk).
root.mainloop()                         # Allows for the system to run continually.

