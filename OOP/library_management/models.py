import settings
import pickle
from uuid import uuid4

from db import BaseQuery

class MetaBase(type):
    
    def __init__(self, *args, **kwargs):
        self.query = BaseQuery(self.file_path)
        super().__init__(*args, **kwargs)


#### Users
class BaseUser(metaclass=MetaBase):
    type = None
    file_name = None
    file_path = None


    def __init__(self, username, password) -> None:
        self.username = username
        self.password = self._set_password(password)
        self.id = self._generate_id()

    @staticmethod
    def _generate_id():
        return str(uuid4())


    @staticmethod
    def _set_password(passw):
        return hash(passw)
    

    def save(self):
        try:
            with open(settings.USER_DATA_PATH / self.file_name, "ab") as db_file:
                pickle.dump(self, db_file)

        except Exception as e:
            print(e)


class Admin(BaseUser):
    type = "Admin"
    file_name = "admins.db"
    file_path = settings.USER_DATA_PATH / file_name

    def add_user(self):
        pass


class Member(BaseUser):
    type = "Member"
    file_name = "members.db"
    file_path = settings.USER_DATA_PATH / file_name



### Books
class BaseBook(metaclass=MetaBase):
    file_name = None
    file_path = None


    def __init__(self, name, author) -> None:
        self.name = name
        self.author = author
        self.id = self._generate_id()

    @staticmethod
    def _generate_id():
        return str(uuid4())


    def save(self):
        try:
            with open(settings.BOOKS_DATA_PATH / self.file_name, "ab") as db_file:
                pickle.dump(self, db_file)

        except Exception as e:
            print(e)


class Book(BaseBook):
    file_name = "books.db"
    file_path = settings.BOOKS_DATA_PATH / file_name

