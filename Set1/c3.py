def get_score(string):
    freq = {
        'e': 57, 'a': 43, 'r': 38, 'i': 38, 'o': 36,
        't': 35, 'n': 34, 's': 29, 'l': 28, 'c': 23,
        'u': 18, 'd': 17, 'p': 16, 'm': 15, 'h': 15,
        'g': 12, 'b': 10, 'f': 9, 'y': 9, 'w': 6,
        'k': 5, 'v': 5, 'x': 1, 'z': 1, 'j': 1,
        'q': 1, ' ': 70
    }
    
    score = 0
    for byte in string.lower():
        score += freq.get(chr(byte),0)

    return score

def single_byte_xor(key_byte,coded_string):
    xored_bytes = b''

    for byte in coded_string:
        xored_bytes += bytes([byte ^ key_byte])

    return xored_bytes

def detect_single_byte_xor(coded_string):
    max_score = 0
    max_score_str = b''

    for key_byte in range(256):
        xored_bytes = single_byte_xor(key_byte,bytes.fromhex(coded_string))

        score = get_score(xored_bytes)
        if score > max_score:
            max_score = score
            max_score_str = xored_bytes
        
    return max_score_str

def main():
    str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    print(detect_single_byte_xor(str))
if __name__ == "__main__":
    main()