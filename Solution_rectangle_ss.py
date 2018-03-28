
class Rectange():
    def __init__(self, longueur=0 , largeur=0):
        self.large = largeur
        self.long = longueur
        self.nom="rectange"
    def Surface (self):
        return self.long*self.large
    def __str__(self):
        return ("\nle {} de cotes {} et {} a une surface de {}"._format(self.nom, self.long, self.large, self.surface()))



class Carre(Rectange):
    def __init__(self, cote=0):
        Rectange.__init__(self, cote,cote)
        super().__init__(cote, cote)
        self.cot = cote
        self.nom ="carre"


a = Rectange(12,8)
#print(a)
#a.Surface()
#a.__str__()
print(a.Surface())
b= Carre(456)
print(b.Surface())