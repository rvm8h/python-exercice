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
            a = match.group(groupNum).strip('\n')

        groupNum = groupNum + 1

        #print("Group {groupNum} found: {group}".format(groupNum=groupNum, group=match.group(groupNum)))

        if groupNum == 2:
            b = match.group(groupNum).strip(r'\n')
            print('a =',a,',b =',b)
            Dickus[a] = int(b)

        #print(Dickus)

#output sorted dictionary
print('Dictionary:',Dickus,'\nSorted Dictionary:',sorted(Dickus))

file.close()