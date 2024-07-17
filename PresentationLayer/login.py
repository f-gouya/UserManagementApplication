from tkinter import Frame, Label, Entry, Button, messagebox
from BusinessLayer.user_business_logic import UserBusinessLogic


class LoginFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.main_view = view

        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Login Form")
        self.header.grid(row=0, column=1, pady=10, sticky="w")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")
        self.username_entry.insert(0, "farzad.gouya")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="w")

        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")
        self.password_entry.insert(0, "P@ssw0rd")

        self.login_button = Button(self, text="Login", width=10, command=self.login)
        self.login_button.grid(row=3, column=1, pady=(0, 10), sticky="w")

        self.register_button = Button(self, text="Register", width=10, command=self.show_register_frame)
        self.register_button.grid(row=3, column=1, pady=(0, 10), padx=(0, 20), sticky="e")

    def show_register_frame(self):
        register_frame = self.main_view.switch_frame("register")
        register_frame.clear_register_entry()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user_business = UserBusinessLogic()
        response = user_business.login(username, password)

        if not response.success:
            messagebox.showerror("Error", response.message)
        else:
            self.clear_login_entry()
            home_frame = self.main_view.switch_frame("home")
            home_frame.set_current_user(response.data)

    def clear_login_entry(self):
        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
