# cipher_methods/vigenere_cipher.py
def vigenere_cipher(text, key):
    key = key.upper()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - 65
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

def vigenere_decipher(text, key):
    key = key.upper()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = 26 - (ord(key[key_index]) - 65)
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result
