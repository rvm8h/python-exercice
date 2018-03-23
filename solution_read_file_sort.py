# ouvrir le fichier data.txt
# lire les objets et valeurs
# et mettre les objets et valeurs dans un dictionnaire
# trier le dictionnaire par valeur

dictionnary= {}
f = open("data.txt", 'r')

lines = f.readlines()     # lit toutes les lignes d'un coup
print(lines)
f.close()   # ferme le fichier
for l in lines:
    line = l.rstrip()   # enleve le caratere \n de fin de ligne
    items = line.split(",") # retourne une liste avec 2 valeurs
    items[0]=items[0].replace(" ","")
    dictionnary[items[0]]=int(items[1])  # assigne les valeurs, converties en int,  au dictionnaire,

# tri par sur les keys
for t in sorted(dictionnary):
    print (t, ' =>', dictionnary[t])
#print(dictionnary)

# tri sur les valeurs
#for t in sorted(dictionnary.values()):
#    print (t)

# tri sur les valeurs
t = [(v, k) for k, v in dictionnary.items()]
t.sort()
t= [(k, v) for v, k in t]
#print(t)
for it in t:
    print(it)

# tri sur les valeurs
from operator import itemgetter

a = sorted(dictionnary.items(), key=itemgetter(1))
print(a)
