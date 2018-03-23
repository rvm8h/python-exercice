#Initialisez deux entiers : a = 0 et b = 10.
#Écrire une boucle affichant et incrémentant la valeur de a tant qu’elle reste inférieure
#à celle de b.
#Écrire une autre boucle décrémentant la valeur de b et affichant sa valeur si elle est
#impaire. Boucler tant que b n’est pas nul.


# programme principal -----------------------------------------------
a, b = 0, 10
while a < b:
    print(a, end=" ")
    a += 1

print("\n\nAutre exemple :\n")
while b: # signifie : tant que b est vrai (i-e b non nul)
    b -= 1
    if b % 2 != 0:
        print(b, end=" ")
print()