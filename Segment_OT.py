# Définir une classe Point avec un constructeur fournissant les coordonnées par défaut d’un point du plan (par exemple : x = 0.0 et y = 0.0).
# Définir une classe Segment dont le constructeur possède quatre paramètres : deux pour l’origine et deux pour l’extrémité.
# Ce constructeur définit deux attributs : orig et extrem, instances de la classe Point.
# De cette manière, vous concevez une classe composite : La classe Segment est composée de deux instances de la classe Point.
# Ajouter une méthode d’affichage.
# Enfin écrire un auto-test (__str__) qui affiche une instance de Segment initialisée par les valeurs 1, 2, 3 et 4.

class Point:

    def __init__(self, x = 0.0, y = 0.0):

        self.x = x
        self.y = y

    def display(self):
        return "Point de coordonnée: x = {} et y = {}".format(self.x, self.y)


class Segment:
    def __init__(self,x1, y1,x2,y2):

        self.orig = Point(x1,y1)
        self.extrem = Point(x2,y2)

    def display(self):
        print ("a = x : {}, y : {} et b = x : {}, y : {}".format(self.orig.x, self.orig.y, self.extrem.x, self.extrem.y))

    def __str__(self):
        return "Segment de point a = x : {}, y : {} et b = x : {}, y : {}".format(self.orig.x,self.orig.y,self.extrem.x,
                                                                                 self.extrem.y)

x = Segment(1,2,3,4)
x.display()
print(x)