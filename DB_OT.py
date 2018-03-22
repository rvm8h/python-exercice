#Écrivez un script qui crée un mini-système de base de données fonctionnant à l’aide d’un dictionnaire, dans lequel vous
#mémoriserez les noms d’une série de copains, leur âge et leur taille.

#Votre script devra comporter deux fonctions : la première pour le remplissage du dictionnaire, et la seconde pour sa
#consultation. Dans la fonction de remplissage, utilisez une boucle pour accepter les données entrées par l’utilisateur.

#Dans le dictionnaire, le nom de l’élève servira de clé d’accès, et les valeurs seront constituées de tuples (âge, taille),
#dans lesquels l’âge sera exprimé en années (donnée de type entier), et la taille en mètres (donnée de type réel).

#La fonction de consultation comportera elle aussi une boucle, dans laquelle l’utilisateur pourra fournir un nom quelconque
#pour obtenir en retour le couple « âge, taille » correspondant.

#Le résultat de la requête devra être une ligne de texte bien formatée, telle par exemple : « Nom : Jean - age : 15 ans - taille : 1. 74 m


#V1
#dictionary setting
database = dict()

#functions definitions
def DatabaseIn(name, age, height):

    database[name] = age, height

    return database


def DatabaseOut(name):

    age = database[name][0]
    height = database[name][1]

    return print("Nom :" , name , "- age :" , age , "- taille : ",height,"m")


#filling db
while 1:

    name = input("entrez un nom: ")
    if name == "":
        print("breaking")
        break

    age = int(input("entrez un âge: "))
    height = float(input("entrez une taille: "))

    DatabaseIn(name,age,height)

print(database)


#requesting db
while 1:

    NameIn = input("Recherche: ")
    if NameIn == "":

        print("breaking")
        break
    else:
        DatabaseOut(NameIn)


#V2
def DbIn():

    while 1:

        name = input("entrez un nom: ")
        if name == "":
            print("breaking")
            break
        else:
            age = int(input("entrez un âge: "))
            height = float(input("entrez une taille: "))
            database[name] = age, height

    return print(database)

def DbOut():

    while 1:

        NameIn = input("Recherche: ")
        if NameIn == "":

            print("breaking")
            break
        else:

            age = database[NameIn][0]
            height = database[NameIn][1]
            print("Nom :", NameIn, "- age :", age, "- taille : ", height, "m")

    return

DbIn()
DbOut()