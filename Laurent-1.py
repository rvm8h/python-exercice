#!/usr/bin/env python3

#Mettre les lignes du fichier texte dans un dictionnaire
#Version avec un type d'objet unique "valeur" recherché sur toutes les lignes du fichier
l=[]
mydic={}
#close implicite dans le for
for line in open('data.txt'):
    if 'valeur' == line.split(',')[0] :
        l.append(int(line.split(',')[1]))
l.sort()
mydic={'valeur':l}
print(mydic)


#Version avec des types d'objets différents triés par noms, chacun avec leur nombre :
lTypes=[]
lNumbers=[]
mydic={}
#close implicite dans le for
for line in open('data.txt'):
        lTypes.append(line.split(',')[0].replace(' ',''))
        lNumbers.append(int(line.split(',')[1]))
mydic=dict(zip(lTypes, lNumbers))
lNumbers=[]
for key in sorted(mydic):
    lNumbers.append(mydic[key])
lTypes.sort()
mydic=dict(zip(lTypes, lNumbers))
print(mydic)


#Création d'un fichier ne contenant que les chaines WARNING du fichier jenkins.dat
l=[]
with open('jenkins.dat', 'r', encoding='utf-8') as fIn:
    for line in fIn.readlines():
        if "WARNING" in line:
            l.append(line)
fOut=open('laurent.ret', 'w', encoding='utf-8')
fOut.writelines(l)
fOut.close()

