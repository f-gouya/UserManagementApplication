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

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
