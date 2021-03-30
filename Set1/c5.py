def repeating_byte_xor(key,coded_string):
    xored_bytes = b''
    counter = 0
    for byte in coded_string:
        xored_bytes += bytes([byte ^ key[counter % len(key)]])
        counter += 1

    return xored_bytes


def main():
    key = "ICE"
    str = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    
    hex_xored_bytes = repeating_byte_xor(key.encode(),str.encode()).hex()
    
if __name__ == "__main__":
    main()