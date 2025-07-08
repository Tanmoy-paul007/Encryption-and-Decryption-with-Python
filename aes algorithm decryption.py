from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Same key used for encryption (must match exactly)
key = b'ThisIsASecretKey'

# Encrypted message (example from previous encryption)
# You must have this from the encryption part
ciphertext = b'your_encrypted_bytes_here'

# Create cipher
cipher = AES.new(key, AES.MODE_ECB)

# Decrypt and unpad
plaintext = unpad(cipher.decrypt(ciphertext), 16)

print("Decrypted message:", plaintext.decode())

