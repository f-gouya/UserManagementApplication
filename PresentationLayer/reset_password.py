from ttkbootstrap import Frame, Label, Entry, Button
from ttkbootstrap.dialogs import Messagebox
from BusinessLayer.user_business_logic import UserBusinessLogic


class ResetPasswordFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.main_view = view

        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Reset Password Request")
        self.header.grid(row=0, column=1, pady=10, sticky="w")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.reset_password_button = Button(self, text="Confirm", width=10, command=self.change_password)
        self.reset_password_button.grid(row=4, column=1, pady=(0, 10), sticky="w")

        self.back_button = Button(self, text="Back", width=10, command=self.show_login_frame)
        self.back_button.grid(row=4, column=1, pady=(0, 10), padx=(0, 20), sticky="e")

    def change_password(self):
        username = self.username_entry.get()
        user_business = UserBusinessLogic()
        response = user_business.change_password(username)
        if not response.success:
            Messagebox.show_error(response.message, "Error")
        else:
            Messagebox.show_info(response.message, "Info")
            self.clear_change_password_entry()
            self.show_login_frame()

    def show_login_frame(self):
        login_frame = self.main_view.switch_frame("login")
        login_frame.clear_login_entry()

    def clear_change_password_entry(self):
        self.username_entry.delete(0, "end")
