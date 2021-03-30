def fixed_xor(str1,str2):
    bin_str1 = bin(int(str1, 16))[2:]
    bin_str2 = bin(int(str2, 16))[2:]

    target_length = len(bin_str1) if len(bin_str1) > len(bin_str2) else len(bin_str2)

    bin_str1 = bin_str1.zfill(target_length)
    bin_str2 = bin_str2.zfill(target_length)

    xored_string = ""

    for s1,s2 in zip(bin_str1,bin_str2):
        if (s1 == '0' and s2 == '1') or (s1 == '1' and s2 == '0'):
            xored_string += '1'
        else:
            xored_string += '0'

    return hex(int(xored_string,2))[2:]

def main():
    str1 = "1c0111001f010100061a024b53535009181c"
    str2 = "686974207468652062756c6c277320657965"

    print(fixed_xor(str1,str2))
if __name__ == "__main__":
    main()
