# algorithms.py
def sort_based_cipher(text):
    return ''.join(sorted(text))

def sort_based_decipher(text):
    # Assuming original text before cipher is known and provided for decryption
    return ''.join(sorted(text))

def search_based_cipher(text, keyword):
    # Implement a simple search-based ciphering mechanism
    return ''.join(chr((ord(char) + ord(keyword[i % len(keyword)]) - 2 * ord('A')) % 26 + ord('A'))
                   for i, char in enumerate(text.upper()))

def search_based_decipher(text, keyword):
    return ''.join(chr((ord(char) - ord(keyword[i % len(keyword)]) + 26) % 26 + ord('A'))
                   for i, char in enumerate(text.upper()))
