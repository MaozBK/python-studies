
alphabet = "abcdefghijklmnopqrstuvwxyz"


def caesarCipher(text, k):
    cipher_text = ""
    for i in text:
        position = alphabet.find(i)
        new_position = (position + k) % 26
        cipher_text += alphabet[new_position]
    return cipher_text


word = input("Please Enter text for encryption: ")
number = int(input("Please Enter key for encryption: "))

print("the Encrypted text is: " + caesarCipher(word, number))

