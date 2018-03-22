#Initialisez deux entiers : a = 0 et b = 10.

#Écrire une boucle affichant et incrémentant la valeur de a tant qu’elle reste inférieure à celle de b.

#Écrire une autre boucle décrémentant la valeur de b et affichant sa valeur si elle est impaire. Boucler tant que b n’est pas nul.

a = 0
b = 10

while a < b:
    a += 1

print("first loop ended successfully\n")

while b != 0:
    b-= 1
    if b % 2 == False:
        print(b)
