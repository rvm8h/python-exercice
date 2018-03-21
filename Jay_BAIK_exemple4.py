# ouvrir le fichier data.txt
# lire les valeurs
# et mettre les valeurs dans un dictionnaire
# trier le dictionnaire par valeur

file = open('data.txt', 'r')
text = file.read()
dic = dict()
list = text.split('\n')

for i in list:
    p = i.split(',')
    dic[p[0]] = int(p[1])
for key in sorted(dic):
    print(key, '=>', dic[key])

file.close()