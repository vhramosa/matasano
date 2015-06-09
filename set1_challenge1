''' http://cryptopals.com/sets/1/challenges/1/ '''
test_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
should_produce = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
base64_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']

bin_string = ""
base64_string = ""

''' Translate hex to binary '''
for i in range(0, len(test_string), 2):
    bin_string += str(bin(int(test_string[i:i+2], base=16))[2:].zfill(8))
    
''' Take 6 binary digits each time and map to base64 alphabet'''
for i in range(0, len(bin_string), 6):
    index = int(bin_string[i:i+6], 2)
    base64_string += base64_alphabet[index]

'''In case of padding'''
for i in range(len(base64_string) % 4):
    base64_string += '='

print base64_string
