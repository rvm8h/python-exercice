#!/usr/bin/env python

# Exercice de mini base de donnees
# nom de l'eleve : cle
# age, taille : valeurs


# dictionnaire est initializé en dehors de fonctions (global)
data = {}

# fonction input
def input_dict():
    temp = []
    print("Please enter name, age and height: ")

    for x in range(3):
        inp = input()
        temp.append(inp)

    key = temp[0]
    tup = (int(temp[1]), float(temp[2]))
    data[key] = tup
    print("The data has been updated: ")
    print(data)

# fonction consultation
def view_dict():
    print("Search by name: ")
    name = input()
    values = list(data.values())
    print("Nom : " + name + " - Age: " + str(values[0][0]) + " ans - Taille: " + str(values[0][1]) + " m")

# test
input_dict()
view_dict()


