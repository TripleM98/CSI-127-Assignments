def freq(n,l):
    numbers = 0
    for x in l:
        if x == n:
            numbers=numbers+1
    return numbers


def min(l):
    number = l[0]
    for x in l:
        if x < number:
            number=x
    return number


def mode(l):
    highest = 0
    highest_val = 0
    for x in l:
        freq2 = freq(x,l)
        if freq2 > highest_val:
            highest = x
            highest_val = freq2
    return highest

print(freq('2',['2', '2', '3','2', '6']))
print(min(['6','1','4']))
print(mode(['5','5','4','3','2','5']))