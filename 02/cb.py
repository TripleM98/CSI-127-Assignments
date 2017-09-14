def string_times(str, n):
    result=''
    x=0
    while(x<n):
        result+=str
        x+=1
    return result
##########################################################################################################

def front_times(str, n):
    result=''
    x=0
    while (x<n):
        result+=str
        x+=1
    return result


############################################################################################################


def string_bits(str):
    return str[0:2]
    
    
    
############################################################################################################
    
def lone_sum(a, b, c):
  sum=a+b+c
  if(a==b==c):
    return 0
  elif(a==b):
      return c
  elif(b==c):
      return a
  elif(a==c):
      return b
  elif(a!=b!=c):
      return sum
#############################################################################################################
    
def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result = result + str[:i+1]
  return result
  
    
##############################################################################################################
    
def cigar_party(cigars, is_weekend):
  if(cigars>=40 and cigars<=60 and not is_weekend):
    return True 
  elif(cigars>=40 and is_weekend):
    return True
  else:
    return False

##############################################################################################################
def caught_speeding(speed, is_birthday):
  if(speed<=60 and not is_birthday):
    return 0
  elif(speed>=61 and speed<=80 and not is_birthday):
    return 1
  elif(speed>=81 and not is_birthday):
    return 2
  elif(speed==60 and is_birthday):
    return 0
  elif(speed==85 and is_birthday):
    return 1
  elif(speed==75 and is_birthday):
    return 1
  elif(speed==40 and is_birthday):
    return 0


