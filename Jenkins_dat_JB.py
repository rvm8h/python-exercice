#!/usr/bin/env python
import re

# Ouvrir les deux fichier en mode R et W
jenkins = open('jenkins.dat', 'r')
myfile = open('BAIK.ret', 'w')

# Lire le fichier jenkins.dat, trouver les warnings
for line in jenkins:
    if re.search("WARNING", line):
        myfile.write(line)

# Verification de fichier
myfile = open('BAIK.ret', 'r')
for line in myfile:
    print(line)