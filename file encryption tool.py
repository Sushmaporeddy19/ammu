from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open
def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted)
    print(f"{filename} encrypted successfully.")

def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(filename, "wb") as dec_file:
        dec_file.write(decrypted)
    print(f"{filename} decrypted successfully.")

def main():
    while True:
        print("\n=== File Encryption/Decryption Tool ===")
        print("1. Generate Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            generate_key()
            print("Key generated and saved as 'secret.key'.")
        elif choice == "2":
            if not os.path.exists("secret.key"):
                print("Key file not found! Generate key first.")
                continue
            filename = input("Enter the file name to encrypt: ")
            if not os.path.exists(filename):
                print("File does not exist.")
                continue
            key = load_key()
            encrypt_file(filename, key)
        elif choice == "3":
            if not os.path.exists("secret.key"):
                print("Key file not found! Generate key first.")
                continue
            filename = input("Enter the file name to decrypt: ")
            if not os.path.exists(filename):
                print("File does not exist.")
                continue
            key = load_key()
            decrypt_file(filename, key)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
