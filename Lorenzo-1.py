# Ouvrir le fichier data.txt
# et mettre les valeurs dans un dictionnaire

l = []

for line in open('data.txt'):
        l.append(int(line.split(',')[1]))
d={'Valeurs': l}
print(d)
