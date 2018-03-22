#!/usr/bin/env python

# Exercice sur les boucles while

a = 0
b = 10

# while n.1
while a < b:
    print("La valeur de a: " + str(a))
    a = a + 1

print("\n")

# while n.2
while b != 0:
    b = b - 1
    if b % 2 == 1:
        print("La valeur de b: " + str(b))