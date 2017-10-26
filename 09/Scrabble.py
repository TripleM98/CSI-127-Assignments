#This problem is still incomplete. The maximum sum return is always 4 no matter how long the string is.

def score(w):
  Scrabble_Points={
      1:'AEIOULNRST',
      2:'DG',
      3:'BCMP',
      4:'FHVWY',
      5:'K',
      8:'JX',
      10:'QZ'  }

  w = w.upper()
  sum=0
  for characters in w:
    for points in Scrabble_Points.keys():
       while characters in Scrabble_Points[points]:
            New_Sum=sum+points
            return w, New_Sum


print(score('hello'))
  

 