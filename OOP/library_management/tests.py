from models import Admin, Member
import pickle
import settings
# admin_object = Admin("asghar", "1234")
# member_object = Member("akbar", "1234")


# admin_object.save()
# member_object.save()

def loadall(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break


items = loadall(settings.USER_DATA_PATH / "admins.db")


for item in items:
    print(item.username)
    print(item.password)

# dbfile = open(settings.USER_DATA_PATH / "admins.db", 'rb')     
# db = pickle.load(dbfile)

# for elm in db:
#     print(elm.username)

# dbfile.close()



