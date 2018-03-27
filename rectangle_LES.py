# creer une class Retangle
# prend 2 parameters long , larg , par default  = 0
# une methode surface
# une methode __str__ pour l 'affichage avec
# ces caracteriques lon , larg ,surface

class Rectangle:

    def __init__(self, long = 0, larg = 0):
        self.long = long
        self.larg = larg
        self.nom = "rectangle"

    def __str__(self):
        return 'Le {} de cotes {} et {} a une surface de {}'.format(self.nom, self.long, self.larg, self.surface())

    def surface(self):
        return self.long*self.larg

class Carre(Rectangle):

    def __init__(self, cote = 0):
        #super().__init__(cote, cote)
        Rectangle.__init__(self, cote, cote)
        self.nom = "carre"

rectangle=Rectangle(5,10)
print(rectangle)
# x.larg = 7
# print(x.surface())

carre = Carre(5)
print(carre)
carre.surface()