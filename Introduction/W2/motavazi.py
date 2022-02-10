def motavazi(width, height):
    # for i in range(height):
    #     if i==0:
    #         print(" " * height + "*" * width)
    #     elif i != height -1:
    #         print(" " * (height - i) + "*" + " " * (width - 2) + "*")
    #     else:
    #         print(" " + "*" * width)


    print(" " * height + "*" * width)
    for i in range(1, height -1):
        print(" " * (height - i) + "*" + " " * (width - 2) + "*")
    print(" " + "*" * width)


motavazi(4, 5)



def cesar_cipher(plain_text: str, key: str) -> str:
    ascii_key = ord(key.lower())
    result = ""
    for char in plain_text.lower():
        if char == " ":
            result += " "
        else:
            result += chr(((ord(char) % 97 + ascii_key % 96) % 26) + 97)
       
    return result






def decipher(cipher_text: str, key: str) -> str:
    ascii_key = chr((122 - ord(key.lower())) + 96)
    result = cesar_cipher(cipher_text, ascii_key)
    return result

if __name__ == "__main__":
    key = "b"
    plain = "zxmn tur"
    print("plain text: ", plain)
    cipher  = cesar_cipher(plain, key)
    print("cipher text: ", cipher)
    print("plain bad ramz goshai: ", decipher(cipher, key))
