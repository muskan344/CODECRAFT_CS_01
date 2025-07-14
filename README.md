# CODECRAFT_CS_01

This particular repository is about a task given to me during my internship in codecraft. I have developed my skills in CyberSecurity through this Internship. The task implemented in this repo is "Implementing Caeser Cipher".  

The Brief of the given task is Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

## Project Structure
Caesar_Cipher/
  ├── caesar_cipher.py
  └── README.md

## Setup

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/Caesar_Cipher.git
cd Caesar_Cipher
```

## 2. Run the program

```bash
python caesar_cipher.py
```

## Usage
When you run the script, you’ll be prompted to:

- Choose between encryption or decryption  
- Enter your message  
- Enter the shift value (e.g., 3)

## Example 
```bash
=== Caesar Cipher Encryption & Decryption === 
Type 'encrypt' to encrypt or 'decrypt' to decrypt: encrypt
Enter your message: Hello World!
Enter shift value (e.g., 3): 3
Encrypted Message: Khoor Zruog!
``` 

## Output 
- This implementation only shifts alphabetical characters (A-Z, a-z).
- Spaces, punctuation, and digits are not affected by the cipher.

## Future Improvements
- Add GUI or web interface for interaction.
- Add support for file-based input/output encryption.
- Include Caesar Cipher brute-force decryption option.


