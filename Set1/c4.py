from c3 import get_score,detect_single_byte_xor

def main():
    file = open("c4.txt", "r")
    encoded_strings = file.read().split('\n')
    
    max_score = 0
    max_score_string = b''
    
    for encoded_string in encoded_strings:
        decoded_string = detect_single_byte_xor(encoded_string)
        decoded_string_score = get_score(decoded_string)

        if decoded_string_score > max_score:
            max_score = decoded_string_score
            max_score_string = decoded_string
    
    print(max_score_string)

if __name__ == "__main__":
    main()