#I am lost on what to do next. To be more specific, I am having difficulty imagining the next steps for what the code should look like.

TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10), (7,7))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

def make_scrabble_board():
    board=[]
    for i in range(15):
        line=[]
        for i in range(15):
            line.append('_')
        board.append(line)

    for r,c in TRIPLE_WORD_SCORE:
        board[r][c] = 'T'

    for r,c in DOUBLE_WORD_SCORE:
        board[r][c] = 'D'

    for r,c in TRIPLE_LETTER_SCORE:
        board[r][c]='t'

    for r,c in DOUBLE_LETTER_SCORE:
        board[r][c] = 'd'
    return board


def print_board(b):
    for line in b:
        print ( ' '.join(line))

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
  return sum
def add_word_across(board,word,r,c):
    
    values ={
    "aeioulnrst":1, 
    "dg": 2,
    "bcmp":3,
    "fhvwy":4,
    "k":5,
    "jx":8,
    "qz":10}

    word = word.lower()
    sum=0
    score_of_character= 0
    w_multiplier = 1
    if(len(board[r]) - c < len(word)):
        print("This word is too long.")
        return sum
    else:
        i = 0
        for characters in word:
            for x in values:
                if characters in x:
                    score_of_character=values[x]
            if(board[r][c+i] == 't'):
                char_score *= 3
            elif(board[r][c+i] == 'd'):
                score_of_character*= 2
            elif(board[r][c+i] == 'T'):
                w_multiplier *= 3
            elif(board[r][c+i] == 'D'):
                word_multiplier *= 2
            board[r][c+i] = characters
            sum+= score_of_character
            score_of_character= 0
            i += 1
    return sum* w_multiplier


def add_word_down(board,word,r,c):
    
    values = {
    "aeioulnrst" : 1,
    "dg"         : 2,
    "bcmp"       : 3,
    "fhvwy"      : 4,
    "k"          : 5,
    "jx"         : 8,
    "qz"         : 10
    }

    word = word.lower()
    sum=0
    score_of_character= 0
    word_multiplier = 1
    if(len(board[r]) - r < len(word)):
        print("This word doesn't fit!")
        return sum
    else:
        i = 0
        for characters in word:
            for k in values:
                if characters in k:
                    score_of_character = values[k]
            if(board[r+i][c] == 't'):
                score_of_character *= 3
            elif(board[r+i][c] == 'd'):
                score_of_character*= 2
            elif(board[r+i][c] == 'T'):
                w_multiplier *= 3
            elif(board[r+i][c] == 'D'):
                w_multiplier *= 2
            board[r+i][c] = char
            sum+=score_of_character
            score_of_character= 0
            i += 1
    return sum* w_multiplier

#Test cases
y= make_scrabble_board()
print("Score:",add_word_across(y,"HELLO",0,5))
print_board(y)
g=make_scrabble_board()
print("Score:",add_word_across(g, "SFLJwrgrwhufvbd",0,0))
print_board(g)


