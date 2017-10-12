import math
real_stats = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]

def rotate_char(c,r):
    v = ord(c)
    v = v - 97
    v = (v + r)%26
    v = v + 97 
    result = chr(v)
    return result

def encode_string(s,r):
    result = ""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            letter = rotate_char(letter,r)
        result = result + letter
    return result

def full_encode(s):
    n = ''
    for i in range(26):
        n = n + encode_string(s,i) + "\n"
    return n


def distance (List1, List2):
    length = len(List1)
    if length > len(List2):
        length = len (List2)
    sum = 0
    for i in range (length):
        sum = sum + ((List1[i] - List2[i])*(List1[i]-List2[i]))
    d = math.sqrt(sum)
    return d

def build_frequency_vector(s):
    spaces = s.count(' ')
    num_letters = len(s) - spaces
    v=[]
    for letter in "abcdefghijklmnopqrstuvwxyz":
        v.append(s.count(letter) / num_letters)
    return v

def print_vector_table(v):
    s="abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        print(s[i],":",str(v[i]))

def decode(s):
    distance2=1
    x=len('abcdefghijklmnopqrstuvwxyz') 
    while distance(real_stats, build_frequency_vector(encode_string(s,x))) < distance2:
        distance2=distance(real_stats, build_frequency_vector(encode_string(s,x)))
        Location=encode_string(s,x)
    return Location
        

z='what is going on'
print(decode(z))
print('encoded: ', encode_string(z, 13))


f = open('48320-0.txt')
x = f.read()
x = x.lower()
real_stats = build_frequency_vector(x)
f.close()

print('decoded:',decode(z))

