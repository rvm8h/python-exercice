# ouvrir le fichier data.txt
# lire les valeurs
# et mettre les valeurs dans un dictionnaire
# trier le dictionnaire par valeur

# Version 1
file = open('data.txt', 'r')
text = file.read()
file.close()

dict = dict()
list = text.split('\n')

for i in list:
    p = i.split(',')
    newP = p[0].split(' ')
    dict[newP[0]] = int(p[1])

print("Voici le tableau trie par valeur: \n")
for key in sorted(dict, key=dict.get):
    print(key, '=>', dict[key])