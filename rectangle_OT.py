# creer une class Retangle
# prend 2 parameters long , larg , par default  = 0
# une methode surface
<<<<<<< HEAD
# une methode __str__ pour l 'affichage avec
# ces caracteriques lon , larg ,surface



class rectangle:

    def __init__(self, long = 0, larg = 0):
        self.long = long
        self.larg = larg
        self.nom = "rectangle"

    def surface(self):

        self.surface = self.larg * self.long
        return self.surface

    def __str__(self):
        return "{} Longeur: {}, Largeur: {}, Surface: {}".format(self.nom, self.long, self.larg, self.surface())

class carre(rectangle):

    def __init__(self, cote = 0):
        rectangle.__init__(self,cote, cote)
        self.nom = "carré"



x = rectangle()
y = rectangle(3,2)
z = carre(2)




print(x)
print(y)
print(z)

=======
#une methode __str__ pour l 'affichage avec
#ces caracteriques lon , larg ,surface



class rectangle():
    def __init__(self, long = 0, larg = 0):
        self.long = long
        self.larg = larg

    def surface(self):
        self.surface = self.larg * self.long

    def __str__(self):
        return "Longeur: {}, Largeur: {}, Surface: {}".format(self.long, self.larg, self.surface)

x = rectangle()
x.surface()

y = rectangle(3,2)
y.surface()

print("x =", x ,"\n y =", y)
>>>>>>> origin/Olivier
