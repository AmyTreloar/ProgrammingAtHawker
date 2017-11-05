from tkinter import *


class AuthorisedUser(object):
    def __init__(self, name, account_number, pin):
        self.name = name
        self.account_number = account_number
        self.pin = pin


class BankingApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("800x600+300+0")
        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.authed_user = None

        self.frames = {}

        for F in [AuthenticationFrame]:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("AuthenticationFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.draw_frame()
        frame.tkraise()


class CommonFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.drawn = False


class AuthenticationFrame(CommonFrame):
    def __init__(self, parent, controller):
        CommonFrame.__init__(self, parent, controller)

    def draw_frame(self):
        if self.drawn:
            return
        self.drawn = True;
        width = self.winfo_width()
        height = self.winfo_height()
        username = Entry(self)
        username.insert(0, "Username")
        username.bind("<Button-1>", lambda _: self.clear_entry(username))
        username.place(x=360, y=260)
        password = Entry()
        password.insert(0, "Password")
        password.bind("<Button-1>", lambda _: self.clear_entry(password))
        password.place(x=360, y=300)
        username.focus()
        authenticate = Button(self, text="Authenticate", command=lambda _: self.authenticate_user(username, password))
        authenticate.place(x=420, y=340)
        cancel = Button(self, text="Cancel", command=lambda _: self.cancel_authentication(username, password))
        cancel.place(x=360, y=340)

    def cancel_authentication(self, username_entry, password_entry):
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        username_entry.insert(0, "Username")
        password_entry.insert(0, "Password")

    def authenticate_user(self, username_entry, password_entry):
        pass

    def clear_entry(self, entry):
        entry.delete(0, END)


class UserAccount(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller


if __name__ == "__main__":
    app = BankingApp()
    app.mainloop()
