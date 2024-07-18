from tkinter import Frame, Label, Entry, Button, messagebox
from BusinessLayer.user_business_logic import UserBusinessLogic


class ResetPasswordFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.main_view = view

        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Reset Password Request")
        self.header.grid(row=0, column=1, pady=10, sticky="w")

        self.old_password_label = Label(self, text="Old Password")
        self.old_password_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")

        self.old_password_entry = Entry(self)
        self.old_password_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.new_password_label = Label(self, text="New Password")
        self.new_password_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="w")

        self.new_password_entry = Entry(self)
        self.new_password_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.confirm_password_label = Label(self, text="Confirm Password")
        self.confirm_password_label.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="w")

        self.confirm_password_entry = Entry(self)
        self.confirm_password_entry.grid(row=3, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.reset_password_button = Button(self, text="Confirm", width=10)
        self.reset_password_button.grid(row=4, column=1, pady=(0, 10), sticky="w")

        self.back_button = Button(self, text="Back", width=10)
        self.back_button.grid(row=4, column=1, pady=(0, 10), padx=(0, 20), sticky="e")
