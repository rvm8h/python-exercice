#s1 = 'SPAM' s2 = 'SCAM'
#Ecrire une fonctions qui retourne une liste contenant les carateres communs a ces 2 listes

s1 = 'SPAM'
s2 = 'SCAM'

def Comparator(x,y):

    list1 = list(x)
    list2 = list(y)
    listout = []

    for a in range(len(list1)):

        for b in range(len(list2)):
            if list1[a] == list2[b]:
                listout.append(list1[a])
    return print(listout)

Comparator(s1,s2)
