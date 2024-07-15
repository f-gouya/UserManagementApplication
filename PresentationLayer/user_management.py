from tkinter import Frame, Label, Button, Entry
from tkinter.ttk import Treeview
from BusinessLayer.user_business_logic import UserBusinessLogic


class UserManagementFrame(Frame):
    def __init__(self, window):
        super().__init__(window)

        self.row_list = []
        self.current_user = None
        self.user_business = UserBusinessLogic()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.header = Label(self, text="User Management Form")
        self.header.grid(row=0, column=0, pady=10)

        self.search_entry = Entry(self, width=30)
        self.search_entry.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")

        self.search_button = Button(self, text="Search", command=self.search)
        self.search_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        self.activate_button = Button(self, text="Activate", command=self.activate)
        self.activate_button.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

        self.deactivate_button = Button(self, text="Deactivate", command=self.deactivate)
        self.deactivate_button.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="w")

        self.user_table = Treeview(self, columns=("firstname", "lastname", "username", "status"))
        self.user_table.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="nsew")

        self.user_table.heading("#0", text="NO")
        self.user_table.heading("#1", text="First Name")
        self.user_table.heading("#2", text="Last Name")
        self.user_table.heading("#3", text="Username")
        self.user_table.heading("#4", text="Status")

    def search(self):
        term = self.search_entry.get()
        user_list = self.user_business.search(self.current_user, term)
        self.fill_table(user_list)

    def activate(self):
        user_id_list = self.user_table.selection()
        for user_id in user_id_list:
            self.user_business.activate(self.current_user, user_id)

        user_list = self.load_data()
        self.fill_table(user_list)

    def deactivate(self):
        user_id_list = self.user_table.selection()
        for user_id in user_id_list:
            self.user_business.deactivate(self.current_user, user_id)

        user_list = self.load_data()
        self.fill_table(user_list)

    def set_current_user(self, user):
        self.current_user = user
        user_list = self.load_data()
        self.fill_table(user_list)

    def load_data(self):
        user_list = self.user_business.get_users(self.current_user)
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
