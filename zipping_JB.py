#!/usr/bin/env python

li = []
file = 'email.txt'

with open(file) as infile:
    line = infile.read().split('\n')
    print(line[0])
