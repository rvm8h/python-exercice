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

# Exercise 1

dic = dict()

file = open('data.txt', 'r')
lines = file.readlines()
print ('Lignes du fichier %s : %s' % (file.name, lines))

for row in lines:
    item = row.split(',')
    key = item[0].replace(' ','')
    val = int(item[1].rstrip('\n'))
    dic[item[0]] = int(item[1])

print(dic)

for key in sorted(dic):
    print(key, '=>', dic[key])

print (dic)

file.close()

# Exercise 2

file = open('jenkins.dat', 'r')
lines = file.readlines()
print(lines)
file.close()

file = open('lorenzo.ret', 'w')
file.write('test')

file.close()

