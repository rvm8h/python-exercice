# creer une class Retangle
# prend 2 parameters long , larg , par default  = 0
# une methode surface
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