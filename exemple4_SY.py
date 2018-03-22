#!/usr/bin/python
import re
dict= {}
file = open('data.txt','r')
print("nom du fichier : " , file.name)
for line in file :
    print(line)

for line in file :
    nline=line.rstrip()
    var = nline.split(",")
    val= var[0].replace("","")
    dict[val]= int(var[1])

    print('tab sans tri')
    print(dict)
    print("\n")

    t = [(v, k) for k, v in dict.items()]
    t.sort()

    print(" trié par valeur: ")
    t = [(k, v) for v, k in t]
    print(t)


 #creation fichier warning
J=[]
with open('jenkins.dat', 'r', encoding='utf-8') as fIn:
       for line in fIn.readlines():
           if "WARNING" in line:
               J.append(line)
with open('sy.ret', 'w', encoding='utf-8') as fOut:
       fOut.writelines(J)




#boucle while

b = 10# On garde la variable contenant le nombre dont on veut la table de multiplication
a = 0 # C'est notre variable compteur que nous allons incrémenter dans la boucle

while a < 10: # Tant que i est strictement inférieure à 10
    print(a + 1, "*", b, "=", (a + 1) * b)
    a += 1 # On incrémente i de 1 à chaque tour de boucle

 #boucle affichant le nombre s'il est impair

c = 9

while c != 0:   # tant que le c est different de zero

 c -= 1     #decrementé c
 if c % 2 == True:      # verifier le reste de la division

     print(c)    # afficher C

# base de donnée

 #creation tableau vide
mondic= dict()

 # fonction remplissage du dictionnaire
def remplir(nom, age ,taille):
 for line in dict:
     line[nom]
     line[age]
     line[taille]

 #fonction de consultation
def consultation():
      for line in dict:
          line.get["nom"]
          line.get["age"]
          line.get["taille"]
          return print(line)


          

mondic={}
mondic[("age","taille")] ="nom"