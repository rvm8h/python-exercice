# Creer une classe Rectangle
# prenant deux parametres long, larg par defaut = 0
# une methode surface
# une methode __str__ pour l affichage avec ces caracteristiques long, larg, surface
#
class Rectangle():
    long = 0
    larg = 0

    def __init__(self, long, larg):
        self.long = long
        self.larg = larg

    def surface(self):
        return (self.long * self.larg)

    def __str__(self):
        print("Long = {}".format(self.long))
        print("Larg = {}".format(self.larg))
        print("Surface = {}".format(self.surface()))


class Carre(Rectangle):

    def __init__(self):
        super.__init__()
        self.nom = 'carre'


rect01 = Rectangle(4, 3)
rect02 = Rectangle(6, 3)
# rect03 = Rectangle(,)
rect02.__str__()
rect01.surface()

print('carré')

carr01 = Carre(2, 2)
carr01.__str__()