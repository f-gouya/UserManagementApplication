from CommonLayer.response import Response
from CommonLayer.decorators import Decorator
from DataAccessLayer.user_data_access import UserDataAccess
from CommonLayer import global_variables
from CommonLayer.user import User
import hashlib

decorator = Decorator()


class UserBusinessLogic:
    def __init__(self):
        self.user_data_access = UserDataAccess()
        self.hash_string = None

    @decorator.execution_time_log
    def login(self, username, password):
        if len(username) < 4 or len(password) < 8:
            return Response(None, False, "Invalid inputs.")
        hash_password = self.password_hashing(password)
        user = self.user_data_access.get_user(username, hash_password)
        if not user:
            return Response(None, False, "Invalid username or password.")
        if not user.status:
            return Response(None, False, "Your account is not active.")
        return Response(user, True)

    @decorator.execution_time_log
    def enrollment(self, firstname, lastname, username, password):
        try:
            user = User(None, firstname, lastname, username, password, 0, 1, 0)
        except ValueError as e:
            return Response(None, False, f"{e}")

        # if len(password) < 8:
        #     return Response(None, False, "Password must be complex and at least 8 characters.")
        if self.check_username_exist(username):
            return Response(None, False, "This username already exists.")
        else:
            hash_password = self.password_hashing(password)
            self.user_data_access.add_new_user(firstname, lastname, username, hash_password)
            return Response(None, True, f"Your account is created successfully.\n"
                                        f"Please contact the Administrator to activate your account.")

    @decorator.execution_time_log
    def change_password(self, username):
        if len(username) < 4:
            return Response(None, False, "Username must be at least 4 characters.")
        elif not self.check_username_exist(username):
            return Response(None, False, "The username was not found.")
        else:
            self.user_data_access.update_request(username)
            return Response(None, True, f"Your request was sent to the administrator.\n"
                                        f"Please contact the Administrator to confirm your request.")

    @decorator.execution_time_log
    def get_user_request(self):
        if global_variables.current_user.role_id == 2:
            user_list = self.user_data_access.get_all_request()
            return user_list

    @decorator.execution_time_log
    def get_users(self):
        if global_variables.current_user.role_id == 2:
            user_list = self.user_data_access.get_all_users(global_variables.current_user.id)
            return user_list

    @decorator.execution_time_log
    def deactivate(self, user_id):
        if global_variables.current_user.role_id == 2:
            self.user_data_access.update_status(user_id, 0)

    @decorator.execution_time_log
    def activate(self, user_id):
        if global_variables.current_user.role_id == 2:
            self.user_data_access.update_status(user_id, 1)

    @decorator.execution_time_log
    def search(self, term):
        if global_variables.current_user.role_id == 2:
            user_list = self.user_data_access.search(term)
            return user_list

    @decorator.execution_time_log
    def check_username_exist(self, username):
        username_exist = self.user_data_access.check_unique_username(username)
        if username_exist:
            return True

    @decorator.execution_time_log
    def confirm_user_request(self, user_id):
        hash_password = self.password_hashing("P@ssw0rd")
        if global_variables.current_user.role_id == 2:
            self.user_data_access.update_password(user_id, hash_password)

    @decorator.execution_time_log
    def password_hashing(self, password):
        self.hash_string = hashlib.md5(password.encode())
        hash_password = self.hash_string.hexdigest()
        return hash_password
