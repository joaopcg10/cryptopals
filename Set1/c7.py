import base64
from Crypto.Cipher import AES

def decrypt_aes(key,encoded):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(encoded)

    return plaintext

def main():
    file = open("c7.txt", "r")
    encoded = base64.b64decode(file.read())

    print(decrypt_aes("YELLOW SUBMARINE".encode(),encoded))
if __name__ == "__main__":
    main()