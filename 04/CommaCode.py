def CommaCode(list):
    
    
    for items in list:
        list[-1]='and '+list[-1]
        return ', '.join(list)
    
print(CommaCode(['Cat', 'dog', 'mouse', 'house', 'blouse', 'clown']))
   
