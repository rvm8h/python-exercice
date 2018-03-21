# ouvrir le fichier data.txt
# lire les valeurs
# et mettre les valeurs dans un dictionnaire
# trier le dictionnaire par valeur

file = open('data.txt', 'r')
text = file.read()
file.close()

dic = dict()
list = text.split('\n')

for i in list:
    p = i.split(',')
    newP = p[0].split(' ')
    dic[newP[0]] = int(p[1])

for key in sorted(dic, key=dic.get):
    print(key, '=>', dic[key])
