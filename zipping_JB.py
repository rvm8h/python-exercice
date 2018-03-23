#!/usr/bin/env python
from itertools import islice
li = []
file = 'email.txt'

with open(file) as infile:
    key = []
    line = infile.read().split('\n')
    st = line[0].split(',')
    print(st)
    print(infile.readlines()[1:])

