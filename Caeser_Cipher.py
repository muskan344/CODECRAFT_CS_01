def caesar_cipher_encrypt(text,shift):
    result=""
    for char in text:
        if char.isalpha():
            base=ord('A') if char.isupper() else ord('a')
            result+=chr((ord(char)-base+shift)%26+base)
        else:
            result+=char  # Non-alphabetic characters are not changed
    return result

def caesar_cipher_decrypt(text,shift):
    return caesar_cipher_encrypt(text,-shift)

def main():
    print("=== Caesar Cipher Encryption & Decryption ===")
    choice=input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    message=input("Enter your message: ")
    try:
        shift=int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if choice=='encrypt':
        encrypted=caesar_cipher_encrypt(message,shift)
        print(f"Encrypted Message: {encrypted}")
    elif choice=='decrypt':
        decrypted=caesar_cipher_decrypt(message,shift)
        print(f"Decrypted Message: {decrypted}")
    else:
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")

if __name__=="__main__":
    main()
