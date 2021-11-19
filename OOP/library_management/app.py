from controllers import register

print("""

            SALAM..... Be Ketabkhaneh Ketabkhanan Khosh Amadid

""")

while True:
    temp = input("ozvi ya na?(y/n): ")
    if temp == "n":
        print("Bia ozv Shooo!!")
        try:
            username = input("username chi mikhay?")
            password = input("ye passam bezan")
            print(register(username, password))

        except:
            print("shlagham username bayad unique bashe")
            continue

