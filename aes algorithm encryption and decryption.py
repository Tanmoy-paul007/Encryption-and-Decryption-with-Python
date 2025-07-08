from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'ThisIsASecretKey'
message = "Hello, AES encryption!"

# Encrypt
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(message.encode(), 16))
print("Encrypted:", ciphertext)

# Decrypt
cipher = AES.new(key, AES.MODE_ECB)
plaintext = unpad(cipher.decrypt(ciphertext), 16)
print("Decrypted:", plaintext.decode())
