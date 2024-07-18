from CommonLayer.response import Response
from DataAccessLayer.user_data_access import UserDataAccess
from CommonLayer import global_variables
import hashlib


class UserBusinessLogic:
    def __init__(self):
        self.user_data_access = UserDataAccess()

    def login(self, username, password):
        if len(username) < 4 or len(password) < 8:
            return Response(None, False, "Invalid inputs.")
        hash_string = hashlib.md5(password.encode())
        hash_password = hash_string.hexdigest()
        user = self.user_data_access.get_user(username, hash_password)
        if not user:
            return Response(None, False, "Invalid username or password.")
        if not user.status:
            return Response(None, False, "Your account is not active.")
        return Response(user, True)

    def enrollment(self, firstname, lastname, username, password):
        if len(firstname) < 3 or len(lastname) < 3:
            return Response(None, False, "Invalid inputs.")
        elif len(username) < 4:
            return Response(None, False, "Username must be at least 4 characters.")
        elif len(password) < 8:
            return Response(None, False, "Password must be complex and at least 8 characters.")
        elif self.check_username_exist(username):
            return Response(None, False, "This username already exists.")
        else:
            hash_string = hashlib.md5(password.encode())
            hash_password = hash_string.hexdigest()
            self.user_data_access.add_new_user(firstname, lastname, username, hash_password)
            return Response(None, True, f"Your account is created successfully.\n"
                                        f"Please contact the Administrator to activate your account.")

    def change_password(self, username):
        if len(username) < 4:
            return Response(None, False, "Username must be at least 4 characters.")
        elif not self.check_username_exist(username):
            return Response(None, False, "The username was not found.")
        else:
            self.user_data_access.update_request(username)
            return Response(None, True, f"Your request was sent to the administrator.\n"
                                        f"Please contact the Administrator to confirm your request.")

    def get_user_request(self):
        if global_variables.current_user.role_id == 2:
            user_list = self.user_data_access.get_all_request()
            return user_list

    def get_users(self):
        if global_variables.current_user.role_id == 2:
            user_list = self.user_data_access.get_all_users(global_variables.current_user.id)
            return user_list

    def deactivate(self, user_id):
        if global_variables.current_user.role_id == 2:
            self.user_data_access.update_status(user_id, 0)

    def activate(self, user_id):
        if global_variables.current_user.role_id == 2:
            self.user_data_access.update_status(user_id, 1)

    def search(self, term):
        if global_variables.current_user.role_id == 2:
            user_list = self.user_data_access.search(term)
            return user_list

    def check_username_exist(self, username):
        username_exist = self.user_data_access.check_unique_username(username)
        if username_exist:
            return True

    def confirm_user_request(self, user_id):
        hash_string = hashlib.md5("P@ssw0rd".encode())
        hash_password = hash_string.hexdigest()
        if global_variables.current_user.role_id == 2:
            self.user_data_access.update_password(user_id, hash_password)
