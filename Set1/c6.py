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

def min_hamming(hamming_list):
    key_size = 0
    min_ham = 1000

    for i in len(range(hamming_list)):
        if hamming_list[i][0] < min_ham:
            key_size = hamming_list[i][1]

    return key_size


def main():
    file = open("c6.txt", "r")
    encoded = base64.b64decode(file.read())
    min_list = []

    for key_size in range(2,40):
        for i in range(0,len(encoded)-key_size*2,key_size):
            tmp_list = []
            first = encoded[i:i+key_size]
            second = encoded[i+key_size:i+(key_size*2)]
            tmp_list.append(hamming(first,second)/key_size)
        normalized_hamming = (sum(tmp_list) / len(tmp_list))
        min_list.append((normalized_hamming,key_size))
    
    sorted_list = sorted(min_list, key=lambda tup: tup[0])
    possible_key_sizes = [key[1] for key in sorted_list[:4]]

    keys = []
    for key_size in possible_key_sizes:
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

        keys.append(key)

    print("Possible keys are: " + str(keys))
if __name__ == "__main__":
    main()