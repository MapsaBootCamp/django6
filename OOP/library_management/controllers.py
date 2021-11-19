from models import Member

def register(username, password):
    if Member.query.exist("username", username):
        raise Exception("hamchin useri darim!")
    member = Member(username, password)
    member.save()

    return "be khubi va khoshi ozv. ketab bekhun!"