#!/usr/bin/env python3


#Version avec des types d'objets différents triés par noms, chacun avec leur nombre :
lTypes=[]
lNumbers=[]
mydic={}
#close implicite dans le for
for line in open('data.txt'):
        lTypes.append(line.split(',')[0].replace(' ',''))
        lNumbers.append(int(line.split(',')[1]))
mydic=dict(zip(lTypes, lNumbers))
lNumbers=[]
for key in sorted(mydic):
    lNumbers.append(mydic[key])
lTypes.sort()
mydic=dict(zip(lTypes, lNumbers))
print('Dictionnaire trié par noms : ', mydic)



#Version avec des types d'objets différents triés par quantités :
lTypes=[]
lNumbers=[]
mydic={}
for line in open('data.txt'):
        lTypes.append(line.split(',')[0].rstrip())
        lNumbers.append(int(line.split(',')[1]))
mydic=dict(zip(lTypes, lNumbers))
mytuples=[(v, k) for k, v in mydic.items()]
mytuples.sort()
mydic=dict([(v, k) for k, v in mytuples])
print('Dictionnaire trié par quantités : ', mydic)



#Création d'un fichier ne contenant que les chaines WARNING du fichier jenkins.dat
l=[]
with open('jenkins.dat', 'r', encoding='utf-8') as fIn:
    l = (line for line in fIn.readlines() if "WARNING" in line)
with open('laurent.ret', 'w', encoding='utf-8') as fOut:
    fOut.writelines(l)


#Boucles
a, b= 0, 10
while a<b:
    print('valeur de a :', a)
    a += 1
while b>0:
    b -= 1
    if b%2!=0:print('valeur de b : ', b)






#Insertion dans un dictionnaire d'un tuple (nom,taille,age)
def insertDB(name, height, age, dictionnary):
    tuples=[]
    d={}
    record=(name, (float(height), int(age)))
    tuples = [(n, data) for n, data in dictionnary.items()]
    tuples.append(record)
    tuples.sort()
    d=dict([(n, data) for n, data in tuples])
    return d


#Recherche dans un dictionnaire d'un tuple (nom,taille,age) par le nom
def requestDB(name, dictionnary):
    result=()
    if len(dictionnary.keys())==0:
        return ()
    else:
        return dictionnary[name]
    return ()



#Test des primitives insertDB() et requestDB()
dic={}
dic=insertDB('Philippe', 1.75, 24, dic)
dic=insertDB('Paul', 1.70, 38, dic)
dic=insertDB('Marc', 1.85, 29, dic)
print(dic)
individurecherche = 'Philippe'
print(individurecherche, ' : ', requestDB(individurecherche, dic))




#Boucle d'interaction avec un utilisateur en ligne de commande :
def interactiveMenu(dico):
    while 1:
        print('Taper 0 pour consulter le dictionnaire')
        print('Taper 1 pour insérer un enregistrement dans le dictionnaire')
        print('Autre touche pour sortir')
        choice = input()
        if int(choice) == 0:
            print('Entrez le nom recherché :')
            individurecherche = input()
            print(individurecherche, ' : ', requestDB(individurecherche, dico))
        elif int(choice) == 1:
            print('Entrez le nom a insérer :')
            name = input()
            print('Entrez la taille a insérer :')
            height = input()
            print('Entrez l\'age a insérer :')
            age = input()
            dico = insertDB(name, height, age, dico)
            print(dico)
        else:break
    return dico

#Exécution de la boucle interactive avec l'utilisateur
#dic = interactiveMenu(dic)




def presentInList(x, l):
    for e in l:
        if e == x:
            return True
    return False

#Fonction retournant dans une liste les caractères communs aux deux chaines
def commonCharacters(string1, string2):
    if len(string1)<len(string2):
        listString = list(string1)
        strAlgo = string2
    else:
        listString = list(string2)
        strAlgo = string1
    result = []
    for x in listString:
        if x in strAlgo:
            if not presentInList(x, result):
                result.append(x)
    return result


print(commonCharacters('Adamo', 'Coppola dracula'))




#Charger un fichier contenant des noms et des e-mails
def loadEmails(file):
    lDic = []
    lTypes=[]
    with open(file, 'r', encoding='utf-8') as fIn:
        header=fIn.readline()
        columnsNumber = header.count(',')
        for i in range(columnsNumber+1):
            lTypes.append(header.split(',')[i].rstrip())
        content=fIn.readlines()
        linesNumber = len(content)
        lLines=[]
        for i in range(linesNumber):
            lColsForCurrentLine=[]
            for j in range(columnsNumber + 1):
                lColsForCurrentLine.append( content[i].split(',')[j].rstrip() )
            lLines.append(lColsForCurrentLine)
        for i in range(linesNumber):
            lDic.append(dict(zip(lTypes, lLines[i])))
    return lDic


contacts=loadEmails('email.txt')
print(contacts)
print(*contacts)
for contact in contacts:
    print(contact)
    print(*contact)
    print(contact['email'])
    print("email: {email} -- {last}, {first}".format(**contact))
