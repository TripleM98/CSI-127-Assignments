#1. write a routine rle_decode which will decode a list that represents the rle encoding you did on the test. So, the list [2,'a', 3, 'b', 'c', 2,'d']  should return "aabbbcdd"

#You'll have to determine if an element is an int or a char so you'll have to look that up

def encode_revised(s):
    encoded=[]
    while len(s)>1:
        length_of_s=1
        character=s[0]
        while length_of_s<len(s) and s[length_of_s]==character:
            length_of_s+=1
        if length_of_s>=1:
            encoded.append(length_of_s)
        encoded.append(character)
        s=s[length_of_s:]
    return encoded
print(encode_revised('HELLOO'))
