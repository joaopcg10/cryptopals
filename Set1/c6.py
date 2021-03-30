from c3 import detect_single_byte_xor
import base64

def hamming(str1,str2):
    bin_str1 = bin(int(str1.hex(),16))[2:]
    bin_str2 = bin(int(str2.hex(),16))[2:]

    target_length = len(bin_str1) if len(bin_str1) > len(bin_str2) else len(bin_str2)

    bin_str1 = bin_str1.zfill(target_length)
    bin_str2 = bin_str2.zfill(target_length)

    hamming = 0

    for s1,s2 in zip(bin_str1,bin_str2):
        if s1 != s2:
            hamming += 1

    return hamming

def main():
    file = open("c6.txt", "r")
    encoded = base64.b64decode(file.read())
    print(encoded)
    min_list = []
    for key_size in range(2,40):
        first = encoded[0:key_size]
        second = encoded[key_size:key_size*2]
        min_list.append(int(hamming(first,second) / key_size))

    print(min_list)
    key_size = 29
    print("Key Size: " + str(key_size))

    encoded_chunks = []
    for i in range(0,len(encoded),key_size):
        encoded_chunks.append(encoded[i:i+key_size])

    encoded_blocks = [b''] * key_size
    for chunk in encoded_chunks:
            for byte in range(len(chunk)):
                encoded_blocks[byte] += bytes([chunk[byte]])

    
    key = ""
    for block in encoded_blocks:
        key += detect_single_byte_xor(block.hex())[1]

    print("Key: " + key)
    
if __name__ == "__main__":
    main()