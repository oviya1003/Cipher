# app.py
import streamlit as st
from cipher_methods.caesar_cipher import caesar_cipher, caesar_decipher
from cipher_methods.vigenere_cipher import vigenere_cipher, vigenere_decipher
from algorithms import sort_based_cipher, sort_based_decipher, search_based_cipher, search_based_decipher

st.title("Cipher/Decipher Tool Using Algorithms")

option = st.selectbox("Choose an option", ("Cipher", "Decipher"))
method = st.selectbox("Choose a method", ("Caesar", "Vigenere", "Sort-based", "Search-based"))

text = st.text_area("Enter the text")
key = st.text_input("Enter the key (for Vigenere/Search-based methods)")

if option == "Cipher":
    if method == "Caesar":
        shift = st.number_input("Enter the shift value", min_value=1, max_value=25)
        result = caesar_cipher(text, shift)
    elif method == "Vigenere":
        result = vigenere_cipher(text, key)
    elif method == "Sort-based":
        result = sort_based_cipher(text)
    elif method == "Search-based":
        result = search_based_cipher(text, key)
else:
    if method == "Caesar":
        shift = st.number_input("Enter the shift value", min_value=1, max_value=25)
        result = caesar_decipher(text, shift)
    elif method == "Vigenere":
        result = vigenere_decipher(text, key)
    elif method == "Sort-based":
        result = sort_based_decipher(text)
    elif method == "Search-based":
        result = search_based_decipher(text, key)

st.write("Result:", result)

