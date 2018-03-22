#!/usr/bin/env python3


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
print('Dictionnaire trié par noms : ', mydic)



#Version avec des types d'objets différents triés par quantités :
lTypes=[]
lNumbers=[]
mydic={}
for line in open('data.txt'):
        lTypes.append(line.split(',')[0].rstrip())
        lNumbers.append(int(line.split(',')[1]))
mydic=dict(zip(lTypes, lNumbers))
mytuples=[(v, k) for k, v in mydic.items()]
mytuples.sort()
mydic=dict([(v, k) for k, v in mytuples])
print('Dictionnaire trié par quantités : ', mydic)



#Création d'un fichier ne contenant que les chaines WARNING du fichier jenkins.dat
l=[]
with open('jenkins.dat', 'r', encoding='utf-8') as fIn:
    for line in fIn.readlines():
        if "WARNING" in line:
            l.append(line)
with open('laurent.ret', 'w', encoding='utf-8') as fOut:
    fOut.writelines(l)


#Boucles
a=0
b=10
while a<b:
    print('valeur de a :', a)
    a += 1
while b>0:
    b -= 1
    if b%2!=0:print('valeur de b : ', b)

