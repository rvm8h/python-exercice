
class Rectangle:

    def __init__(self, long = 0, larg = 0):
        self.long = long
        self.larg = larg

    def __str__(self):
        return 'Longueur du rectangle = {}, Largeur = {}, Surface = {}'.format(self.long, self.larg, self.surface())

    def surface(self):
        return self.long*self.larg


x=Rectangle(2,5)
print(x)