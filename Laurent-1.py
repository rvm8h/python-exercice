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


#version avec des types d'objets différents triés par noms, chacun avec leur nombre :
l0=[]
l1=[]
l2=[]
mydic={}
#close implicite dans le for
for line in open('data.txt'):
        l0.append(line.split(',')[0])
        l1.append(int(line.split(',')[1]))
mydic=dict(zip(l0, l1))
for key in sorted(mydic):
    l2.append(mydic[key])
l0.sort()
mydic=dict(zip(l0, l2))
print(mydic)
