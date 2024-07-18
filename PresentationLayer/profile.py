from tkinter import Frame, Label, Button


class ProfileFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.main_view = view

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="My Profile")
        self.header.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        self.firstname_label = Label(self, text="First Name")
        self.firstname_label.grid(row=1, column=0, pady=(0, 10), padx=(20, 0), sticky="w")

        self.current_user_firstname_label = Label(self)
        self.current_user_firstname_label.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="w")

        self.lastname_label = Label(self, text="Last Name")
        self.lastname_label.grid(row=2, column=0, pady=(0, 10), padx=(20, 0), sticky="w")

        self.current_user_lastname_label = Label(self)
        self.current_user_lastname_label.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="w")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=3, column=0, pady=(0, 10), padx=(20, 0), sticky="w")

        self.current_user_username_label = Label(self)
        self.current_user_username_label.grid(row=3, column=1, pady=(0, 10), padx=(0, 20), sticky="w")

        self.change_password_button = Button(self, text="Change Password", command=self.show_reset_password_frame)
        self.change_password_button.grid(row=4, column=0, columnspan=2, pady=(0, 10), padx=20, sticky="ew")

        self.back_button = Button(self, text="Back", command=self.show_home_frame)
        self.back_button.grid(row=5, column=0, columnspan=2, pady=(0, 10), padx=20, sticky="ew")

    def show_user_information(self, user):
        self.current_user_firstname_label.config(text=f"{user.first_name}")
        self.current_user_lastname_label.config(text=f"{user.last_name}")
        self.current_user_username_label.config(text=f"{user.username}")

    def show_reset_password_frame(self):
        self.main_view.switch_frame("reset_password")

    def show_home_frame(self):
        frame = self.main_view.switch_frame("home")
        frame.set_home_user()
