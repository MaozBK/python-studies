import random as rand

alphabet = "abcdefghijklmnopqrstuvwxyz"


def newCipher(text, k1, k2):
    cipher_text = ""
    for b in text:
        position = alphabet.find(b)
        new_position = (k1 * position + k2) % 26
        cipher_text += alphabet[new_position]
    return cipher_text


def randomCipher(text, k1):
    k2 = int(rand.randrange(3, 10))
    return newCipher(text, k1, k2)


print(newCipher(input("Enter a text for Encryption: "), int(input("Enter Key number 1 for the encryption: ")),
                int(input("Enter the second key for Encryption: "))))

print(
    randomCipher(input("Enter a text for Random Encryption: "), int(input("Enter Key number 1 for the encryption: "))))
