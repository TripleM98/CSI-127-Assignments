


				Notes

Monday 9-18-17:

We learned how to use list in python. 
Here is one example of how to create a list: List1=[4, 25, 85, 12, 0]
When making a list, make sure to enclose the items in a bracket.
You can also create a list of strings.
For example:List2=[‘Hello’, ‘What’, ‘Good’, ‘Nice’]
You can even make a list with numbers and strings.
Example: List3=[4, 85, ‘What’, ‘Hello’]
Lists can be added together.
Example: List4=List1+List2, which comes out as [4, 25, 85, 12, 0, ‘Hello’, ‘What’, ‘Good’, ‘Nice’]
However, you CANNOT subtract, divide, or multiply lists.
To get the position of a list, do: List1[0]. This will give you the first item in List1, which is 4.
To add a new item to the list, use the .append function.
Example: List2.append(‘Food’)
	    Print(List2) would add the string ‘Food’ to List2 variable.
To slice a list, do:
List1[ :2]. This will only include numbers 4 and 25 in List1. The second item in the list is the stopping point. Remember that the items in a list start at 0, not 1.
To replace items in a list, do:
List1[ :2]=[15, 4]… This will replace the first two items of List1 with 15 and 4. The new List1 would come out as [15, 4, 85, 12, 0]
To remove items in a list, do:
List2[ :3]=[]…. This is an empty set. The first 3 items in List2 will disappear .

Tuesday 9-19-17:

We learned how to create random numbers in python.
To access random numbers, do:

Import Random (which is the best way to access random numbers.)
To select a range of random numbers, use random.randrange function:
Example: random.randrange(10, 100). This will generate a random number from 10 to 99.
If using a list and you want to rearrange all the items in the list, use the random.shuffle function. 
Ex: Flavor=[‘Chocolate’, ‘Vanilla’, ‘Strawberry’]
       a=Random.shuffle(Flavor)
       print(a)
(Here is something we did not learn in class, but is useful)…
To print out one random item from a list, use the random.choice function.
Ex: r=Random.choice(Flavor)
      print(r)
