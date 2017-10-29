def divide(A,B,u):
    try:
      UnitofCake=A/B
      NumofPeople=u/UnitofCake
      return int(NumofPeople)
    except ZeroDivisionError:
        print('Cannot divide by zero.')
    
print(divide(5,10,1))
print(divide(1,4.5,1))
print(divide(2,0,1))