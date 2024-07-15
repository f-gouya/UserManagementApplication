from tkinter import Frame, Label, Entry, Button, messagebox
from BusinessLayer.user_business_logic import UserBusinessLogic


class RegisterFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.main_view = view

        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Register Form")
        self.header.grid(row=0, column=1, pady=10, sticky="w")

        self.firstname_label = Label(self, text="First Name")
        self.firstname_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")

        self.firstname_entry = Entry(self)
        self.firstname_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.lastname_label = Label(self, text="Last Name")
        self.lastname_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="w")

        self.lastname_entry = Entry(self)
        self.lastname_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="w")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=3, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=4, column=0, pady=(0, 10), padx=10, sticky="w")

        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=4, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.submit_button = Button(self, text="Submit", width=10, command=self.enrollment)
        self.submit_button.grid(row=5, column=1, pady=(0, 10), sticky="w")

        self.back_button = Button(self, text="Back", width=10, command=self.show_login_frame)
        self.back_button.grid(row=5, column=1, pady=(0, 10), padx=(0, 20), sticky="e")

    def show_login_frame(self):
        login_frame = self.main_view.switch_frame("login")
        login_frame.clear_login_entry()

    def enrollment(self):
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        user_business = UserBusinessLogic()
        response = user_business.enrollment(firstname, lastname, username, password)
        if response.success:
            messagebox.showinfo("Error", message="")

    def clear_register_entry(self):
        self.firstname_entry.delete(0, "end")
        self.lastname_entry.delete(0, "end")
        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
