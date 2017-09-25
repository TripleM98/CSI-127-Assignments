#Meraz Mamun and Muskan Kapoor

import random

#Story: Big Tommy, a ADJ man wanted to rob a bank. He walked into the bank and pulled out a NOUN. Everyone in the bank started to VERB. The police came, outnumbered
#him, and took out their guns. Big Tommy didn't know what to do and started to VERB2.s

    
ADJ=['BIG', 'CHUBBY', 'SHORT']

a=random.choice(ADJ)

NOUN=['GUN', 'BOMB', 'KNIFE', 'BAT']

n=random.choice(NOUN) 

VERB=['SCREAM', 'RUN', 'CRY']

v=random.choice(VERB)

VERB2=['RUN', 'ATTACK', 'CRY LIKE A BABY']

v2=random.choice(VERB2)

all=a and n and v and v2

print("Big Tommy, a %s"% a,'man wanted to rob a bank.')
print("He walked into the bank and pulled out a %s" %n, '.')
print('Everyone in the bank started to %s' %v, '.')
print('The police came, outnumbering him, and they took out their guns.')
print('Big Tommy did not know what to do and started to %s' %v2, '.')
    
if(v2=='RUN'):
    print('The cops chased after him.')
elif(v2=='ATTACK'):
    print('The cops shot him dead.')
elif(v2=='CRY LIKE A BABY'):
    print('The cops started laughing at him.')
        
    
    



