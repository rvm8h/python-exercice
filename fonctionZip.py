#!/usr/bin/python


#creer une liste contacts vide
#ouvrir le fichier email.txt en lecture
#lire la premiere ligne en applicant strip et split
#vous avez ainsi une liste contenant les headers
#lire les lignes suivantes en applicant la fonction zip ( header, line)
#faire un append dans votre liste contacts du resultat de la fonction zip
#afficher le resultat au format
#email: <value>  --  lastname ,  firstname
#utiliser l'outil python console pour mettre au point votre structure de donnees


import re



with open("email.txt","r") as mail:
    l = list()
    l = mail.readlines()
    header = l[0].rstrip().split(",")
    print(header)

    for k in l:
        if "first" not in k:
            l.append(zip(header,k.rstrip().split(",")))
        print(l)

for k in l:
    B , J = zip(*k)
    print("email", J[2], "--", J[1], J[0])