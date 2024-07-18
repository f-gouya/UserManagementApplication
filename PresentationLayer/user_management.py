from tkinter import Frame, Label, Button, Entry
from tkinter.ttk import Treeview
from BusinessLayer.user_business_logic import UserBusinessLogic


class UserManagementFrame(Frame):
    def __init__(self, window, view):
        super().__init__(window)

        self.main_view = view

        self.row_list = []
        self.user_business = UserBusinessLogic()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.header = Label(self, text="User Management Form")
        self.header.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        self.back_button = Button(self, text="Back", width=15, command=self.show_home_frame)
        self.back_button.grid(row=0, column=0, pady=10, padx=10, sticky="e")

        self.search_entry = Entry(self, width=30)
        self.search_entry.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="ew")
        self.search_entry.bind("<KeyRelease>", self.search)

        self.activate_button = Button(self, text="Activate", width=15, command=self.activate)
        self.activate_button.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="w")

        self.deactivate_button = Button(self, text="Deactivate", width=15, command=self.deactivate)
        self.deactivate_button.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

        self.user_table = Treeview(self, columns=("firstname", "lastname", "username", "status"))
        self.user_table.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="nsew")

        self.user_table.heading("#0", text="NO")
        self.user_table.heading("#1", text="First Name")
        self.user_table.heading("#2", text="Last Name")
        self.user_table.heading("#3", text="Username")
        self.user_table.heading("#4", text="Status")

    def search(self, _):
        term = self.search_entry.get()
        user_list = self.user_business.search(term)
        self.fill_table(user_list)

    def activate(self):
        user_id_list = self.user_table.selection()
        for user_id in user_id_list:
            self.user_business.activate(user_id)

        user_list = self.load_data()
        self.fill_table(user_list)

    def deactivate(self):
        user_id_list = self.user_table.selection()
        for user_id in user_id_list:
            self.user_business.deactivate(user_id)

        user_list = self.load_data()
        self.fill_table(user_list)

    def set_management_user_info(self):
        user_list = self.load_data()
        self.fill_table(user_list)

    def load_data(self):
        user_list = self.user_business.get_users()
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
                                                 user.username,
                                                 "Active" if user.status else "Inactive"))
            self.row_list.append(row)
            row_number += 1

    def show_home_frame(self):
        frame = self.main_view.switch_frame("home")
        frame.set_home_user()
