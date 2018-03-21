# Ouvrir le fichier data.txt
# et mettre les valeurs dans un dictionnaire

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
