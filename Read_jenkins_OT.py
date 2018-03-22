#lire le fichier jenkins.dat avec la commande with open(filename) as file
#ouvrir un fichier <votre_nom>.ret en ecriture
#avec une liste comprehension selectionner que les lignes qui contiennent WARNING
#ecrire toutes ces lignes dans le fichier <votre_nom>.ret


file = open("jenkins.dat","r")
output = open("Tran_Olivier.ret", "w")
#split file in lines
data = file.read().split("\n")
print(data)
#split lines in sub elements
for x in range(len(data)):

    data.append(data[x].split("\t"))

#looking for warnings and writing new file
for x in range(len(data)):

    for y in range(len(data[x])):
        if data[x][y].find("WARNING") != -1:
            print("warning found:",str(data[x]).replace("[","").replace("]",""))
            output.write(str(data[x]).replace("[","").replace("]",""))


print(data)







file.close()
output.close()