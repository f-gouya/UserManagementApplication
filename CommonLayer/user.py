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
            raise ValueError("The first name must be at least 3 characters and contain only letters.")
        else:
            self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str) or len(value) < 3 or not value.isalpha():
            raise ValueError("The last name must be at least 3 characters and contain only letters.")
        else:
            self._last_name = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or len(value) < 4:
            raise ValueError("The username must be at least 4 characters.")
        else:
            self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str) or len(value) < 8:
            raise ValueError("The password must be complex and at least 8 characters.")
        else:
            self._password = value

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
