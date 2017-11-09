def remove_non_alpha(w):
    result=""
    for l in w:
        if l.isalpha():
            result = result + l
    return result
def build_word_dict(wordlist):
    d={}
    for w in wordlist:
        d.setdefault(w,0)
        d[w] = d[w] + 1
    return d


def build_word_count(f):
    text = open(f).read()
    l=[]
    for w in text.split():
        w = remove_non_alpha(w)
        l.append(w)
    d = build_word_dict(l)
    return d
def sequence_of_words(text):
     list_of_words=[]
     words={}
     text = open(text).read()
     for word in text.split():
         word = remove_non_alpha(word)
         list_of_words.append(word)
        
     for x in range(len(list_of_words)):
         words.setdefault(list_of_words[x],[])
         if(x< len(list_of_words)-1):
            words[list_of_words[x]].append(list_of_words[x+1])
     return words
     
     
d=build_word_count("hamlet.txt") 
print(sequence_of_words("hamlet.txt"))