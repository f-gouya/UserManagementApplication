from CommonLayer.response import Response
from DataAccessLayer.user_data_access import UserDataAccess
import hashlib


class UserBusinessLogic:
    def __init__(self):
        self.user_data_access = UserDataAccess()

    def login(self, username, password):
        if len(username) < 3 or len(password) < 6:
            return Response(None, False, "Invalid input.")
        hash_string = hashlib.md5(password.encode())
        hash_password = hash_string.hexdigest()
        user = self.user_data_access.get_user(username, hash_password)
        if not user:
            return Response(None, False, "Invalid username or password.")
        if not user.status:
            return Response(None, False, "Your account is not active.")
        return Response(user, True)

    def get_users(self, current_user):
        if current_user.role_id == 2:
            user_list = self.user_data_access.get_all_users(current_user.id)
            return user_list

    def deactivate(self, current_user, user_id):
        if current_user.role_id == 2:
            self.user_data_access.update_status(user_id, 0)

    def activate(self, current_user, user_id):
        if current_user.role_id == 2:
            self.user_data_access.update_status(user_id, 1)

    def search(self, current_user, term):
        if current_user.role_id == 2:
            user_list = self.user_data_access.search(term)
            return user_list
