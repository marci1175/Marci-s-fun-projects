from cryptography.fernet import Fernet
import cryptography.fernet
encry_key = Fernet.generate_key()
dontes = input("Enter text, which you want to encrypt, decrypt!\n")
#make sure its not stored anywhere else than memory!!!
cipher_suite = Fernet(encry_key)
#use bytes(f"{dontes}", encoding="ascii") to put a variable in byte
encry_val = cipher_suite.encrypt(bytes(f"{dontes}", encoding="ascii"))
print(encry_val.decode())
#self test (make sure the usage is b"" , .decode() to remove byte format (---> b"asd"))

#decryption (make sure encry_key is en Fernet() usage see: -name- = Fernet(encry_key))
decry_val = cipher_suite.decrypt(encry_val)

print(decry_val.decode())