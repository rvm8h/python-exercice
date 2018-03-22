#!/usr/bin/env python

def intersection(s1, s2):
    list = []
    for x in s1:
        for y in s2:
            if x == y:
              list.append(x)
    print("Voici les caracateres communs : ")
    print(list)

intersection('span', 'scan')