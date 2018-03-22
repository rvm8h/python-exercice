#ouvrir un fichier data.txt
#lire les valeurs
#mettre les valeurs dans un dictionnaire
#trier le dictionnaire par valeur
import re

#opening input file
file = open('data.txt', 'r')
#print(file.read())

#reading input file
List = file.read()

#regex declaration
regex = r"(.*),(.*)\n?"

#regex matches iterations
matches = re.finditer(regex, List)

#dictionary declaration
Dickus = dict()

#input values into dictionary
for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    for groupNum in range(0, len(match.groups())):
        if groupNum == 1 :
            a = match.group(groupNum).strip("\n").replace(" ","")

        groupNum = groupNum + 1

        #print("Group {groupNum} found: {group}".format(groupNum=groupNum, group=match.group(groupNum)))

        if groupNum == 2:
            b = match.group(groupNum).strip("\n").replace(" ","")
            print('a =',a,',b =',b)
            Dickus[a] = int(b)

        #print(Dickus)

#output sorted dictionary
print('Dictionary:',Dickus,'\nSorted Dictionary:',sorted(Dickus),'\n\n')

file.close()


#opening input file
file = open('data.txt', 'r')

#reading input file
lines = file.readlines()

#dictionary
Dickus = dict()

#deleting \n
for x in range(len(lines)):
   lines[x] = lines[x].strip("\n").split(",")

   for y in range(len(lines[x])):
       lines[x][y] = lines[x][y].replace(" ","")

#filling dictionary
for x in range(len(lines)):
    Dickus[lines[x][0]] = int(lines[x][1])



sortval = []
sortkey = []
#retrieving dictionnary values
for x in Dickus:
    sortval.append(Dickus[x])
    sortkey.append(x)


#sort by value
for x in range(len(sortval)):

    for y in range(len(sortval)):

        if sortval[x] < sortval[y]:
            a = sortval[x]
            b = sortkey[x]
            sortval[x] = sortval[y]
            sortval[y] = a
            sortkey[x] = sortkey[y]
            sortkey[y] = b

#output
print('Dictionary:', Dickus, '\nSorted by keys:', sorted(Dickus),'\nSorted by values',sortval)

print('\nby keys:')
for x in sorted(Dickus):
    print(x,'=',Dickus[x])

print('\nby values:')
for x in range(len(sortval)):
    print(sortval[x] , '=' , sortkey[x])

file.close()