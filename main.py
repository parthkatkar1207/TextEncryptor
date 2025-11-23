
from cipher import encrypt_custom, decrypt_custom
import random
import string

def generate_random_key(length):
    
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

print("--- Text Encryptor ---")
while True:
    
    print("Enter the mode:")
    print("1 - Encryption!")
    print("2 - Decryption!")
    print("3 - Exit!")
    mode = input("Choose mode: ").lower()
    if mode == "3":
        print("Goodbye!")
        break
    if mode == "1":
        Message = input("Message: ")
        try:
           Length = int(input("Set the length of key:"))
           if Length <= 0:
            print("Key length must be positive.")
            continue
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
            continue
        key = generate_random_key(Length)  
        print(f"Randomly generated key (need to decrypt your text): {key}")
        cipher_text = encrypt_custom(Message, key)
        print("Encrypted Message:", cipher_text)
    
    elif mode == "2":
        Message = input("Encrypted Message: ")
        key = input("Key (enter the same string that was generated during encryption): ")
        plain_text = decrypt_custom(Message, key)
        print("Decrypted Message:", plain_text)
    else:
        print("Invalid mode. Try again.")
    print()
