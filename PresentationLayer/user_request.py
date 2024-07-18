from tkinter import Frame, Label, Button
from tkinter.ttk import Treeview
from BusinessLayer.user_business_logic import UserBusinessLogic


class UserRequestFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.main_view = view

        self.row_list = []
        self.user_business = UserBusinessLogic()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.header = Label(self, text="User Request Form")
        self.header.grid(row=0, column=0, pady=10)

        self.confirm_button = Button(self, text="Confirm", width=15, command=self.confirm_request)
        self.confirm_button.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="w")

        self.back_button = Button(self, text="Back", width=15, command=self.show_home_frame)
        self.back_button.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

        self.user_table = Treeview(self, columns=("firstname", "lastname", "username"))
        self.user_table.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="nsew")

        self.user_table.heading("#0", text="NO")
        self.user_table.heading("#1", text="First Name")
        self.user_table.heading("#2", text="Last Name")
        self.user_table.heading("#3", text="Username")

    def set_user_request_info(self):
        user_list = self.load_data()
        self.fill_table(user_list)

    def load_data(self):
        user_list = self.user_business.get_user_request()
        return user_list

    def fill_table(self, user_list):
        for row in self.row_list:
            self.user_table.delete(row)
        self.row_list.clear()

        row_number = 1
        for user in user_list:
            row = self.user_table.insert("",
                                         "end",
                                         iid=user.id,
                                         text=str(row_number),
                                         values=(user.first_name,
                                                 user.last_name,
                                                 user.username))
            self.row_list.append(row)
            row_number += 1

    def show_home_frame(self):
        frame = self.main_view.switch_frame("home")
        frame.set_home_user()

    def confirm_request(self):
        user_id_list = self.user_table.selection()
        for user_id in user_id_list:
            self.user_business.confirm_user_request(user_id)

        user_list = self.load_data()
        self.fill_table(user_list)
