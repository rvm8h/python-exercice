
'''
Définir une classe Point avec un constructeur fournissant les coordonnées par défaut d’un point du plan
(par exemple : x = 0.0 et y = 0.0).
Définir une classe Segment dont le constructeur possède quatre paramètres : deux pour l’origine et deux pour l’extrémité.
Ce constructeur définit deux attributs : orig et extrem, instances de la classe Point. De cette manière,
vous concevez une classe composite : La classe Segment est composée de deux instances de la classe Point.
Ajouter une méthode d’affichage.
Enfin écrire un auto-test (__str__) qui affiche une instance de Segment initialisée par les valeurs 1, 2, 3 et 4.
'''


class Point():
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y


class Segment():
    def __init__(self, orig1=0, extrem1=0, orig2=0, extrem2=0):
        self.orig = Point(orig1, orig2)
        self.extrem = Point(extrem1, extrem2)

    def display(self):
        return print("Les coordonnees du segment : {}, {}, {}, {} ".format(self.orig.orig1, self.orig2, self.extrem.extrem1, self.extrem.extrem2))

    def __str__(self):
        print("Les coordonnees du segment : {}, {}, {}, {} ".format(self.orig.orig1, self.orig.extrem1, self.extrem.orig2, self.extrem.extrem2))


seg = Segment(1, 2, 3, 4)
seg.display()
