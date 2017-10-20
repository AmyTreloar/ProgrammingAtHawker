from tkinter import *
from tkinter.ttk import *

class SampleApp(Tk):
    def __init__(self):
        super().__init__()

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (Example1, Example2):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

    def swap(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class Example1(Frame):
    def __init__(self, parent, controller):
       # super().__init__(parent)
        Frame.__init__(self, parent)
        self.controller = controller
        self.initUI()

    def initUI(self):
        # self.style = Style()
        # self.style.theme_use("default")

        #self.master.title("First window")
        #self.pack(fill=BOTH, expand=1)

        swap = Button(self, text="Swap to frame two", command=lambda: self.controller.self.swap())
        swap.place(x=150, y=50)

class Example2(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.initUI()

    def initUI(self):
        # self.style = Style()
        # self.style.theme_use("default")

        #self.master.title("Second window")
        #self.pack(fill=BOTH, expand=1)

        swap = Button(self, text="Swap to frame one", command=lambda: self.controller.self.swap())
        swap.place(x=150, y=50)




def main():
    root = Tk()
    root.geometry("250x250+500+300")
    app = SampleApp()
    root.mainloop()


if __name__ == '__main__':
    main()