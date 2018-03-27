#Créer la classe rectangle
#Qui prend 2 paramètres long et larg, par défaut à 0
#Avec une méthode surface
#Une méthode __str__ pour l'affichage avec ces caractéristiques long, larg et surface


class Rectangle:
    def __init__(self, long=0, larg=0):
        self.long = long
        self.larg = larg
    def __str__(self):
        return '[Rectangle[long : {}, long : {}, surface : {} ]]'.format(self.long, self.larg, self.surface())
    def surface(self):
        return self.long*self.larg
    def display(self):
        print('long : ', self.long, ', larg : ', self.long, ', surface : ', self.surface())

a = Rectangle(4,3)
print(a)
a.display()


class Carre(Rectangle):
    def __init__(self, cote=0):
        self.long = cote
        self.larg = cote

b = Carre(7)
print(b)
b.display()
