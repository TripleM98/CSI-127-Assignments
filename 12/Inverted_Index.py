import csv

def file(s):
    list=[]
    f = open(s)
    file_read=csv.DictReader(f)
    for line in file_read:
        list.append(line)
    f.close()
    return list

def Inverted_Index(x):
    index = {'GOD':(),'SIR':(),'LORD':(),'VICTIM':(),'SORRY':(),'NONE':(), 'FORGIVE':()}
    for items in index:
        Second_List=[]
        for d in list:
            if items.lower() in d['Last Statement']:
                Second_List.append(d['TDCJ Number'])
        index[items] = tuple(Second_List)
    return index

list = file('offenders-clean.csv')
print(Inverted_Index(list))