from cryptography.fernet import Fernet
import os

# Function to generate and save a new key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("A new secret key has been generated and saved as 'secret.key'.")

# Function to load the existing secret key
def load_key():
    if not os.path.exists("secret.key"):
        print("Key not found. Please generate a new key first.")
        return None
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# Encrypt file
def encrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, "rb") as file:
        original_data = file.read()
    encrypted_data = fernet.encrypt(original_data)
    with open(output_file, "wb") as file:
        file.write(encrypted_data)
    print(f"File '{input_file}' encrypted successfully and saved as '{output_file}'.")

# Decrypt file
def decrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception as e:
        print("Decryption failed. Possible reasons: wrong key or corrupted file.")
        return
    with open(output_file, "wb") as file:
        file.write(decrypted_data)
    print(f"File '{input_file}' decrypted successfully and saved as '{output_file}'.")

# Main interface
def main():
    print("\nFile Encryption/Decryption Tool")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    choice = input("Select an option (1/2/3): ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        key = load_key()
        if key:
            input_file = input("Enter the path of the file to encrypt: ")
            output_file = input("Enter the name of the encrypted output file: ")
            encrypt_file(input_file, output_file, key)

    elif choice == "3":
        key = load_key()
        if key:
            input_file = input("Enter the path of the file to decrypt: ")
            output_file = input("Enter the name of the decrypted output file: ")
            decrypt_file(input_file, output_file, key)

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
