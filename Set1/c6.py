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
    str1 = "this is a test"
    str2 = "wokka wokka!!!"

    print(hamming(str1.encode(),str2.encode()))
    
if __name__ == "__main__":
    main()