from tkinter import *

class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Simple")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def centerWindow(self):
        w = 290
        h = 150

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = int((sw - w)/2)
        y = int((sh - h)/2)
        geo = "{}x{}+{}+{}".format(w, h, x, y)
        print(geo)
        self.master.geometry(geo)

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()

main()





















































