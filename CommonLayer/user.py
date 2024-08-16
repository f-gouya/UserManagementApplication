from enum import Enum


class UserStatus(Enum):
    Active = 1
    Inactive = 0


class NameValue:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self._attribute_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._attribute_name]

    def __set__(self, instance, value):
        if (not isinstance(value, str) or len(value) < self.min_length
                or len(value) > self.max_length or not value.isalpha()):
            raise ValueError("The first name and lastname must be at least 3 characters and contain only letters.")
        else:
            instance.__dict__[self._attribute_name] = value


class User:
    first_name = NameValue(3, 20)
    last_name = NameValue(3, 20)

    def __init__(self, uid, firstname, lastname, username, password, status, role_id, request):
        self.id = uid
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self.password = password
        self.status = UserStatus.Active.value if status == 1 else UserStatus.Inactive.value
        self.role_id = role_id
        self.request = request

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

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"

    @classmethod
    def create_instance_tuple(cls, data_tuple):
        if len(data_tuple) < 6:
            user_info = data_tuple + (UserStatus.Inactive.value, 1, 0)
        else:
            user_info = data_tuple

        return cls(user_info[0], user_info[1], user_info[2], user_info[3],
                   user_info[4], user_info[5], user_info[6], user_info[7])
