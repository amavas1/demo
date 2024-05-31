def caesar_cipher_encrypt(text, shift):
    result = ""

    # Traverse the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # If it's not a letter, leave it as it is
        else:
            result += char

    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'E':
        encrypted_text = caesar_cipher_encrypt(text, shift)
        print("Encrypted message:", encrypted_text)
    elif choice == 'D':
        decrypted_text = caesar_cipher_decrypt(text, shift)
        print("Decrypted message:", decrypted_text)
    else:
        print("Invalid choice! Please choose 'E' to encrypt or 'D' to decrypt.")

if __name__ == "__main__":
    main()
