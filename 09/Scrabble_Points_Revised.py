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
        if characters in Scrabble_Points[points]:
            sum=sum+points
  return w, sum

print(score('Hello'))
