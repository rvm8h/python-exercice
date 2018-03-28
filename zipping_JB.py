#!/usr/bin/env python
from itertools import islice
contacts = []
file = 'email.txt'

with open(file) as infile:
    header = infile.readline().strip().split('\n')
    for line in infile:
        line = line.strip().split('\n')
        contacts_map = zip(header, line)
        contacts.append(dict(contacts_map))

print(contacts)
for contact in contacts:
    print("email: {email} -- {last}, {first}".format(**contact))

