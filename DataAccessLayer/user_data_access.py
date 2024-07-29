import sqlite3
from CommonLayer.user import User


class UserDataAccess:
    def __init__(self):
        self.database_name = "Data\\DB\\UMADB.db"

    def get_user(self, username, password):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
            SELECT id,
                   first_name,
                   last_name,
                   username,
                   password,
                   status,
                   role_id,
                   request
            FROM User
            Where username = ?
            And password = ?
            """, (username, password)).fetchone()

            if data:
                user = User(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
                return user

    def get_all_users(self, current_user_id):
        user_list = []
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
            SELECT id,
                   first_name,
                   last_name,
                   username,
                   status,
                   role_id,
                   request
            FROM User
            Where id !=  ?""", (current_user_id,)).fetchall()

            for item in data:
                user = User(item[0], item[1], item[2], item[3], None, item[4] == 1, item[5], item[6])
                user_list.append(user)

        return user_list

    def get_all_request(self):
        user_list = []
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
            SELECT id,
                   first_name,
                   last_name,
                   username
            FROM User
            Where request =  ?
            And role_id !=  ?
            """, (1, 2)).fetchall()

            for item in data:
                user = User(item[0], item[1], item[2], item[3], None, None, None, None)
                user_list.append(user)

        return user_list

    def update_status(self, user_id, new_value):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            Update User
            Set status = ?
            Where id = ?""", (new_value, user_id))

            connection.commit()

    def search(self, term):
        user_list = []
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            query = """
            SELECT id,
                   first_name,
                   last_name,
                   username,
                   status,
                   role_id,
                   request
            FROM User
            WHERE first_name LIKE ?
            OR last_name LIKE ?
            OR username LIKE ?
            """
            cursor.execute(query, (f"%{term}%", f"%{term}%", f"%{term}%"))
            data = cursor.fetchall()

            for item in data:
                user = User(item[0], item[1], item[2], item[3], None, item[4] == 1, item[5], item[6])
                user_list.append(user)

        return user_list

    def add_new_user(self, firstname, lastname, username, password):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            INSERT INTO User (first_name, last_name, username, password)
            VALUES (?, ?, ?, ?);
        """, (firstname.capitalize(), lastname.capitalize(), username, password))

            connection.commit()

    def check_unique_username(self, username):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            query = """
            SELECT username
            FROM User
            WHERE username = ?
            """
            cursor.execute(query, (username,))
            data = cursor.fetchone()
            if data:
                return True

    def update_request(self, username):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            Update User
            Set request = ?
            Where username = ?""", (1, username))

            connection.commit()

    def update_password(self, user_id, new_password):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            Update User
            Set password = ?,
                request = ?
            Where id = ?""", (new_password, 0, user_id))

            connection.commit()

    def record_execution_time(self, function_name, execution_time, call_datetime):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            INSERT INTO Time (function_name, execution_time, call_datetime)
            VALUES (?, ?, ?);
        """, (function_name, execution_time, call_datetime))

            connection.commit()
