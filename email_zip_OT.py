#creer une liste contacts vide
#ouvrir le fichier email.txt en lecture
#lire la premiere ligne en applicant strip et split
#vous avez ainsi une liste contenant les headers
#lire les lignes suivantes en applicant la fonction zip ( header, line)
#faire un append dans votre liste contacts du resultat de la fonction zip
#afficher le resultat au format
#email: <value>  --  lastname ,  firstname
#utiliser l'outil python console pour mettre au point votre structure de donnees



with open("email.txt","r") as mail:
    LContacts = list()
    LContactsL = list()
    list = mail.readlines()
    header = list[0].rstrip().split(",")
    print(header)
    for l in list:
        if "first" not in l:
            LContacts.append(zip(header,l.rstrip().split(",")))
            LContactsL.append(set(zip(header,l.rstrip().split(","))))

    print(LContacts,'\n',LContactsL)
    for l in LContacts:
        H,F = zip(*l)
        print("email:" , F[2] , "--" , F[1], F[0])