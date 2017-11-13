def remove_non_alpha(w): 
    result=""
    for l in w:
        if l.isalpha():
            result = result + l
    return result

def trigram(multiple_words):
    dic_words={}
    for i,words in enumerate(multiple_words):
        if i < len(multiple_words) -3:
            next_words = words + ' ' + multiple_words[i+1] + ' ' + multiple_words[i+2]
            dic_words.setdefault(next_words,[])
            if i == len(multiple_words)-3:
                word = dic_words[next_words]
                dic_words[next_words] = (word[:])
            else:
                dic_words[next_words].append(multiple_words[i+3])
    return dic_words

def trigram_part_2(file):
    text = open(file).read()
    list=[]
    for word in text.split():
        word = word.upper()
        word = remove_non_alpha(word)
        list.append(word)
    return trigram(list)



print(trigram_part_2("hamlet.txt"))
