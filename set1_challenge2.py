'''http://cryptopals.com/sets/1/challenges/2/'''
'''Test strings'''
string1 = "1c0111001f010100061a024b53535009181c"
string2 = "686974207468652062756c6c277320657965"

'''Translate to binary'''
def hexbin(string):    
    bin_string = ""
    for i in range(0, len(string), 2):
        bin_string += str(bin(int(string[i:i+2], base=16))[2:].zfill(8))
    return bin_string

'''Actually the XOR operation'''
xored_string = int(hexbin(string1),2) ^ int(hexbin(string2),2)

'''Format, getting rid of 0x and L characters'''
print hex(xored_string)[2:][:-2]
