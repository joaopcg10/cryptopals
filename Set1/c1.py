import codecs

def hex2b64(hex_string):
    byte_string = bytes.fromhex(hex_string)
    b64_string = base64.b64encode(byte_string)

    return b64_string.decode()

def main():
    print(hex2b64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))

if __name__ == "__main__":
    main()