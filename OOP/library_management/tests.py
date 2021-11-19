from models import Admin, Member, Book
import pickle
import settings

# admin_object = Admin("asghar", "1234")
# member_object = Member("akbar", "1234")


# admin_object.save()
# member_object.save()

# def loadall(filename):
#     with open(filename, "rb") as f:
#         while True:
#             try:
#                 yield pickle.load(f)
#             except EOFError:
#                 break


# items = loadall(settings.USER_DATA_PATH / "admins.db")


# for item in items:
#     print(item.username)
#     print(item.password)

# dbfile = open(settings.USER_DATA_PATH / "admins.db", 'rb')     
# db = pickle.load(dbfile)

# for elm in db:
#     print(elm.username)

# dbfile.close()

# for elm in Member.query.loadall():
#     print(elm.username)


# book_object1 = Book("karamazof", "dastayovski")
# book_object2 = Book("amorshed va margarita", "nabakov")


# book_object1.save()
# book_object2.save()


# for elm in Book.query.loadall():
#     print(elm.name)
#     print(elm.author)


print(Member.query.exist("username", "akbar"))