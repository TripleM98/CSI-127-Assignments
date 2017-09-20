def piglatin(word):
    
    vowel=['a' or 'A', 'e' or'E', 'i' or 'I', 'o' or 'O', 'u' or 'U']
    word = word.lower()
    if(word[0]==vowel):
	#if (word[0] == 'a' or 'e' or 'i' or 'o' or 'u' ):
        
        x=word[0:]+'ay'
        
        return x
           
    newWord=word[1:]+word[0]+'ay'
    
    
    
    return newWord
    
    
print(piglatin('superman'))

    

