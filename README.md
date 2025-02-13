# Ciphering and Deciphering 
## Overview
This project demonstrates a unique approach to ciphering (encryption) and deciphering (decryption) using the MergeSort algorithm and the Divide & Conquer technique. The application is built using Streamlit, a powerful framework for creating interactive web applications with Python. The core idea is to leverage the sorting and merging logic of MergeSort to transform plaintext into ciphertext and vice versa. This method provides a novel way to encrypt and decrypt data, showcasing the versatility of sorting algorithms beyond their traditional use cases.

https://github.com/user-attachments/assets/7acac3d7-61a6-4361-80e8-7bcd28e41fa9


------------

## Features
- **Ciphering:**
   - Encrypts plaintext into ciphertext using a custom implementation of the MergeSort algorithm.

- **Deciphering:**
   - Decrypts ciphertext back into plaintext using the reverse logic of the ciphering process.

- **Divide & Conquer:**
    - Utilizes the Divide & Conquer approach to break down the problem into smaller, manageable subproblems.

- **Python Implementation:**
   - Built entirely in Python, making it easy to understand and extend.
   
- **Streamlit Web App:**
   - Provides an interactive and user-friendly interface for ciphering and deciphering.

------------

## How It Works
**1. Ciphering:**
 - The plaintext is divided into smaller chunks.
 - The plaintext is divided into smaller chunks.
 - Each chunk is processed using a modified MergeSort algorithm to rearrange characters in a specific order, creating ciphertext.
 - The merging logic ensures that the ciphertext is a scrambled version of the original plaintext.

**2. Deciphering:**

- The ciphertext is divided into the same chunks used during ciphering.
- The reverse logic of the MergeSort algorithm is applied to reconstruct the original plaintext.

------------

## Usage
### 1. Clone the repository:
```bash
git clone https://github.com/your-username/cipher-pol.git
cd cipher-pol
```

### 2. Install the required dependencies:
`pip install -r requirements.txt`

### 3. Run the Streamlit app:
`streamlit run app.py`


------------

## License
This project is licensed under the MIT License - see the LICENSE file for details.

------------


## Acknowledgments
- MergeSort algorithm for inspiration.
- Divide & Conquer technique for problem-solving.
- Streamlit for providing an intuitive framework for building interactive web apps.
