from textwrap import wrap
import numpy as np
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Excersize 2-
# a.
def splitTextIntoBlocks(text, key):
    len = key.__len__()
    splited_text = wrap(text, len)
    return splited_text

# b.
def convertBlock(block):
    temp_list = []
    for ch in block:
        temp_list.append(str(alphabet.find(ch.lower()) % 26))
    blockArr = np.array(temp_list)
    return blockArr


def convertKey(key):
    return convertBlock(key)


def encryptionFunc(blockArr, keyArr):
    cipher = []
    i=0
    for ch1 in blockArr:
        cipher.append((int(ch1) + int(keyArr[i])) % 26)
        i += 1
    return np.array(cipher)

def convertArrToText(encryptedArr):
    message = ''
    for element in encryptedArr:
        message += alphabet[int(element)]
    return message

def vigenere(text, key):
    encryptedArr = np.array([])
    keyArr = convertKey(key)
    splitedText = splitTextIntoBlocks(text, key)

    for block in splitedText:
            blockArr = convertBlock(block)
            cipherBlock = encryptionFunc(blockArr, keyArr)
            encryptedArr = np.append(encryptedArr, cipherBlock)
    message = convertArrToText(encryptedArr)
    return message

print("Welcome to Vigenere encryption system!")
text = input("Please enter the text for encryption: ")
key = input("Please enter the key for encryption: ")
print("The encrypted text is: ", vigenere(text, key))
