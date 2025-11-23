import string

def char_to_shift(c):
    # Converts a key character to a shift value: 'A'->0, 'B'->1, ..., 'Z'->25, 'a'->0, ...
    if c.isalpha():
        return ord(c.upper()) - ord('A')
    elif c.isdigit():
        return int(c)
    else:
        return 0

def encrypt_custom(plain_text, key):
    encrypted = ""
    key_len = len(key)
    for i, char in enumerate(plain_text):
        shift = char_to_shift(key[i % key_len])  # Cycle through key characters
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def decrypt_custom(cipher_text, key):
    decrypted = ""
    key_len = len(key)
    for i, char in enumerate(cipher_text):
        shift = char_to_shift(key[i % key_len])
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted
