def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift uppercase and lowercase letters separately
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep non-alphabet characters unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # Just reverse the shift for decryption

# Example usage
message = "Tanmoy"
shift = 3

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print("Original Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
