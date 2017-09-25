def collatz(number):
    if (number % 2 == 0):
        return number//2
    elif(number % 2!=0):
        return number*3+1
try:
    n = int(input('Enter number:'))

    while n>1:
         print (collatz(n))
         n=(collatz(n))
    if(n<1):
        print('You must enter a number greater than or equal to 1.')
except ValueError:
    print('Error: You must enter a number.')