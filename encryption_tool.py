from cryptography.fernet import Fernet

# Step 1: Generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Step 2: Load the saved key
def load_key():
    return open("secret.key", "rb").read()

# Step 3: Encrypt a file
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    
    with open(filename, "rb") as file:
        original = file.read()
    
    encrypted = fernet.encrypt(original)
    
    with open(filename + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted)
    print(f"✅ {filename} encrypted successfully!")

# Step 4: Decrypt a file
def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    
    with open(filename, "rb") as encrypted_file:
        encrypted = encrypted_file.read()
    
    decrypted = fernet.decrypt(encrypted)
    
    output_filename = filename.replace(".enc", "")
    with open(output_filename, "wb") as decrypted_file:
        decrypted_file.write(decrypted)
    print(f"✅ {filename} decrypted successfully!")

# Example Usage
if __name__ == "__main__":
    generate_key()  # Run only once to generate key
    encrypt_file("test.txt")   # Replace with your file name
    decrypt_file("test.txt.enc")
