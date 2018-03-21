#!/usr/bin/env python3

#Mettre les lignes du fichier texte dans un dictionnaire

l=[]
mydic={}
#close implicite dans le for
for line in open('data.txt'): l.append(int(line.split(',')[1]))
l.sort()
mydic={'valeur':l}
print(mydic)
