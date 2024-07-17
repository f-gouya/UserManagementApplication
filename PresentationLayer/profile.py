from tkinter import Frame, Label, Entry, Button, messagebox
from BusinessLayer.user_business_logic import UserBusinessLogic


class ProfileFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.main_view = view

        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="My Profile")
        self.header.grid(row=0, column=1, pady=10, sticky="w")

        self.firstname_label = Label(self, text="First Name")
        self.firstname_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")

        self.lastname_label = Label(self, text="Last Name")
        self.lastname_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="w")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="w")

        self.change_password_button = Button(self, text="Change Password", width=10)
        self.change_password_button.grid(row=4, column=0, pady=(0, 10), sticky="ew")

        self.back_button = Button(self, text="Change Password", width=10)
        self.back_button.grid(row=5, column=0, pady=(0, 10), sticky="ew")
