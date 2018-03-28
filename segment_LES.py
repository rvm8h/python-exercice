# Définir une classe Point avec un constructeur fournissant les coordonnées par défaut d’un point du plan (par exemple : x = 0.0 et y = 0.0).
# Définir une classe Segment dont le constructeur possède quatre paramètres : deux pour l’origine et deux pour l’extrémité.
# Ce constructeur définit deux attributs : orig et extrem, instances de la classe Point.
# De cette manière, vous concevez une classe composite : La classe Segment est composée de deux instances de la classe Point.
# Ajouter une méthode d’affichage. Enfin écrire un auto-test (__str__) qui affiche une instance de Segment initialisée par les valeurs 1, 2, 3 et 4.

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        return "X = {}, Y = {}".format(self.x, self.y)

class Segment():


    def __init__(self, origin, end):
        self.origin = origin
        self.end = end

    def __str__(self):
        return "Origin : {}, End : {}".format(self.origin.display(), self.end.display())

    def display(self):

        print("L'origine est ({}), la fin est ({})".format(self.origin.display(), self.end.display()))


origin = Point(1, 2)
end = Point(3, 4)
segment = Segment(origin, end)

segment.display()
print(segment)
