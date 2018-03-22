#!/usr/bin/python

# Ouvrir le fichier data.txt
# et mettre les valeurs dans un dictionnaire et les trier

l = []
for line in open('data.txt'):
        l.append(int(line.split(',')[1]))
d={'Valeurs': l}
print(d)

#Second version
dic = dict()
file = open('data.txt', 'r')
txt = file.read()
dic = dict()
lst = txt.split('\n')

print('List : ', lst)

for line in lst:
    item = line.split(',')
    dic[item[0]] = int(item[1])

print('Dic : ', dic)

for key in sorted(dic):
    print(key, '=>', dic[key])

file.close()

# Exercise 1 Création d'un dictionnaire trié par valeurs à partir d'un fichier

dic = dict()

file = open('data.txt', 'r')
lines = file.readlines()
file.close()
print ('Lignes du fichier %s : %s' % (file.name, lines))

for row in lines:
    item = row.split(',')
    key = item[0].replace(' ','')
    val = int(item[1].rstrip())
    dic[item[0]] = int(item[1])

for key in sorted(dic):
    print(key, '=>', dic[key])

tup = [(key, val) for key, val in dic.items()]

tup.sort()

dic = dict((x, y) for x, y in tup)

print('Dic trié par clé : ', dic)

tup = [(val, key) for key, val in dic.items()]

tup.sort()

#print (tup)

tup = [(key, val) for val, key in tup]

#print (tup)

dic = dict((y, x) for x, y in tup)

print('Dic trié par valeur : ', dic)

# Exercise 2 Création de fichier avec uniquement des WARNING
lst=[]
file = open('jenkins.dat', 'r')
lines = file.readlines()
file.close()
for line in lines:
    if "WARNING" in line:
        lst.append(line)
out = open('lorenzo.ret', 'w')
out.writelines(lst)
out.close()

# Exercise 3 Boucles while
# Initialisez deux entiers : a = 0 et b = 10.
# Écrire une boucle affichant et incrémentant la valeur de a tant qu’elle reste inférieure à celle de b.
# Écrire une autre boucle décrémentant la valeur de b et affichant sa valeur si elle est impaire. Boucler tant que b n’est pas nul.

a = 0
b = 10

while a < b :
    a += 1
    print("Valeur de a : ", a)

while b > 0 :
    b -= 1
    if b%2!=0:
        print("Valeur de b : ", b)