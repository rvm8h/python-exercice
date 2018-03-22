# ouvrir le fichier data.txt
# lire les valeurs
# et mettre les valeurs dans un dictionnaire
# trier le dictionnaire par valeur

# Version 2
dict = dict()
file = open('data.txt', 'r')
text = file.readlines()
for t in text:
    print(t)