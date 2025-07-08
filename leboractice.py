from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

key = b'tdhcrnkpthygkptf'
mess = input("Enter your Messages:-")

cipher = AES.new(key,AES.MODE_ECB)
enc = cipher.encrypt(pad(mess.encode(),16))
print (enc)

cipher = AES.new(key,AES.MODE_ECB)
dec = unpad(cipher.decrypt(enc),16)
print(dec.decode())