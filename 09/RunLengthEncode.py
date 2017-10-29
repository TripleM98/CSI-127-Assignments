#I could not figure out how to show the letters next to the count.Also, this code only works for lowercase letters from a to z.
def encode(s):
    letters=[0]*26
    for letter in s:
        letters[ord(letter)-ord('a')]+=1
    for item in (letters):
        return s, letters
print(encode('hello'))
        