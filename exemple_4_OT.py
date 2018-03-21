#ouvrir un fichier data.txt
#lire les valeurs
#mettre les valeurs dans un dictionnaire
#trier le dictionnaire par valeur
import re

file = open('data.txt', 'r')
#print(file.read())

List = file.read()
regex = r"(\w*),(.*)\n?"

test_str = ("valeur, 456\nvaleur, 32\nvaleur, 5")

matches = re.finditer(regex, test_str)
Dickus = dict()
for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found: {group}".format(groupNum=groupNum, group=match.group(groupNum)))
        if groupNum == 2:
            a = match.group(groupNum - 1)
            b = match.group(groupNum)
            print(a,',',b)
            Dickus[a] = b

print(sorted(Dickus))

file.close()