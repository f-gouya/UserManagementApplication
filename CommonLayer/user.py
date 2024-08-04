import re


class User:
    def __init__(self, uid, firstname, lastname, username, password, status, role_id, request):
        self.id = uid
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self.password = password
        self.status = True if status == 1 else False
        self.role_id = role_id
        self.request = request

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str) or len(value) < 3 or not value.isalpha():
            raise ValueError("Invalid First name.")
        else:
            self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str) or len(value) < 3 or not value.isalpha():
            raise ValueError("Invalid Last name.")
        else:
            self._last_name = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or len(value) < 4:
            raise ValueError("Invalid username or password.")
        else:
            self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise ValueError("Invalid password.")
        else:
            self._password = value

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
