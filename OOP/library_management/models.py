import settings
import pickle

#### Users
class BaseUser:
    type = None
    file_name = None

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = self._set_password(password)
        self.id = self._generate_id()

    @staticmethod
    def _generate_id():
        pass


    @staticmethod
    def _set_password(passw):
        pass
    

    def save(self):
        try:
            with open(settings.USER_DATA_PATH / self.file_name, "ab") as db_file:
                pickle.dump(self, db_file)

        except Exception as e:
            print(e)


class Admin(BaseUser):
    type = "Admin"
    file_name = "admins.db"

    def add_user(self):
        pass


class Member(BaseUser):
    type = "Member"
    file_name = "members.db"





### Books