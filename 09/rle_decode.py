def rle_decode(list):
    string = ''
    for i, value in enumerate (list):
        if type(value) == int:
            for n in range(value-1):
                string= string+ list[i+1]
        else:
            string += value
    return string

a = [4, 'a', 5, 'b', 1, 'q']
print(rle_decode(a))