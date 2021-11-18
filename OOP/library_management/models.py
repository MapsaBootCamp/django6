# serialize data python


#### Users
class BaseUser:
    type = None

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
        pass

class Admin(BaseUser):
    type = "Admin"

    def add_user(self):
        pass

    def save(self):
        


class Member(BaseUser):
    type = "Member"




### Books
class 