#!/usr/bin/env python

# Version 2 avec readlines()

dict = dict()
file = open('data.txt', 'r')
lines = file.readlines()

for line in lines:
    newLine =line.rstrip()
    datas = newLine.split(',')
    keys = datas[0].replace(" ", "")
    dict[keys] = int(datas[1])
print("Tableau sans tri: ")
print(dict)
print("\n")

# tri sur les valeurs
t = [(v, k) for k, v in dict.items()]
t.sort()

print("Tableau trié par valeur: ")
t = [(k, v) for v, k in t]
print(t)

