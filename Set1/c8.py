from Crypto.Cipher import AES
from c7 import decrypt_aes
from c3 import get_score


def main():
    file = open("c8.txt", "r")
    hex_strings = [bytes.fromhex(line) for line in file.read().split("\n")][:-1]

    freq = []
    for hex_string in hex_strings:
        chunks = []
        for i in range(0,len(hex_string),16):
            chunks.append(hex_string[i:i+16])

        freq.append((hex_string,len(chunks)-len(set(chunks))))    


    freq_sorted = sorted(freq, key=lambda tup: tup[1], reverse=True)

    print(freq_sorted[0])

    """ Possible bruteforce to decode the string but it would take forever...
    target = freq_sorted[0][0]
    score = 0
    decoded = b''
    for i in range(2 ** 1024):
        key = i.to_bytes(16,byteorder="big")
        text = decrypt_aes(key,target)

        if (get_score(text) > score):
            score = get_score(text)
            decoded = text

    print(decoded.decode())
    """

if __name__ == "__main__":
    main()