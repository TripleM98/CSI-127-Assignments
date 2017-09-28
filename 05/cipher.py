import collections
import string

def encode_letter(c,r):

    LowerLetters=collections.deque(string.ascii_lowercase)
    UpperLetters=collections.deque(string.ascii_uppercase)
    
    LowerLetters.rotate(r)
    UpperLetters.rotate(r)
    
    LowerLetters=''.join(list(LowerLetters))
    UpperLetters=''.join(list(UpperLetters))
    
    return c.translate(str.maketrans(string.ascii_lowercase, LowerLetters)).translate(str.maketrans(string.ascii_uppercase, UpperLetters))

print(encode_letter('A, a',-1))
print(encode_letter('A, a', 1))
print('')

#################################################################################################################################################
def encode_strings(s,r):

    LowerLetters=collections.deque(string.ascii_lowercase)
    UpperLetters=collections.deque(string.ascii_uppercase)
    
    LowerLetters.rotate(r)
    UpperLetters.rotate(r)
    
    LowerLetters=''.join(list(LowerLetters))
    UpperLetters=''.join(list(UpperLetters))
    
    return s.translate(str.maketrans(string.ascii_lowercase, LowerLetters)).translate(str.maketrans(string.ascii_uppercase, UpperLetters))

print(encode_strings('Hello there.', -1))
print(encode_strings('Hello there.', 1))
print('')
###################################################################################################################################################

def full_encode(s):
    for l in range (26):
        print(encode_strings(s,l))
        
full_encode('abe')
    
    