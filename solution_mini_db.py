def consultation():
    while 1:
        nom = input("Entrez le nom (ou <enter> pour terminer) : ")
        if nom == "":
            break
        print(nom)
        if nom in dico: # le nom est-il répertorié ?
            item = dico[nom] # consultaion proprement dite
            age, taille = item[0], item[1]
            print ("Nom : %s - âge : %s ans - taille : %s m."\
            % (nom, age, taille))
        else:
            print("*** nom inconnu ! ***")

def remplissage():
    while 1:
        nom = input("Entrez le nom (ou <enter> pour terminer) : ")
        if nom == "":
            break
        age = int(input("Entrez l'âge (nombre entier !) : "))
        taille = float(input("Entrez la taille (en mètres) : "))
        dico[nom] = (age, taille)

dico ={}
while 1:
    choix = input("Choisissez : (R)emplir - (C)onsulter - (T)erminer : ")
    if choix.upper() == 'T':
        break
    elif choix.upper() == 'R':
        remplissage()
    elif choix.upper() == 'C':
        consultation()