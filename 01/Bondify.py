#This line will have the first string as my first and last name.
FirstNameLastName='Meraz Mamun'

#The "split()" function will divide my full name into two parts. The first part will be my first name, which is assigned as 0 and the second part will be my last name, which is assigned as 1.
partnames=FirstNameLastName.split()

#I will combine the two parts as "Last name, first name and last name, which will come out as Mamun, Meraz Mamun.
print(partnames[1]+','+ ' '+partnames[0]+' '+partnames[1])