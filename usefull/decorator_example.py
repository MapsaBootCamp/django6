def gire_bikhod_marzieh():
    print("eshghe marzie! hamechi khareje function")

def khal_ghezi(f):
    print("shirini tavasot sheikh")
    return gire_bikhod_marzieh


def check_arus_umad(func):
    def wrapper():
        print("arus umad")
        func()
        print("dg base.")
    return wrapper

@khal_ghezi
@check_arus_umad
def say_Kel_keshidan():
    print("kilililili!")

# say_Kel_keshidan = check_arus_umad(say_Kel_keshidan)
# say_Kel_keshidan = khal_ghezi(check_arus_umad(say_Kel_keshidan))


say_Kel_keshidan()
say_Kel_keshidan()
say_Kel_keshidan()