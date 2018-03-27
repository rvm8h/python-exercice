# creer une class Retangle prend 2 parameters long , larg , par default  = 0
# une methode surface
# une methode __str__ pour l 'affichage avec ces caracteriques lon , larg ,surface


class Rectangle:
    def __init__(self, long=0, large=0):
        self.long = long
        self.large = large

    def surface(self):
        return self.long * self.large

    def __str__(self):
        return "Longeur : {0}, Largeur: {1}, Surface: {2}".format(self.long, self.large, self.surface())


a = Rectangle()
b = Rectangle(12, 12)

a.surface()
#print(b.surface())

print(a)
print(b)

a.long = 10
a.large = 12

print(a)
