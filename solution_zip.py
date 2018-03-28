# creer une liste contacts vide
# ouvrir le fichier email.txt en lecture
# lire la premiere ligne en applicant strip et split
# vous avez ainsi une liste contenant les headers
# lire les lignes suivantes en applicant la fonction zip ( header, line)
# faire un append dans votre liste contacts vide du resultat de la fonction zip
# afficher le resultat au format
# email: <value>  --  lastname ,  firstname
# utiliser l'outil python console pour mettre au point votre structure de donnees


contacts = []
with open('email.txt') as file:
    header = file.readline().strip().split(',')
    for line in file:
        line = line.strip().split(',')
        contact_map = zip(header, line)
        contacts.append(dict(contact_map))

print(contacts)
print(" ")
for contact in contacts:
    print("email: {email} -- {last}, {first}".format(**contact))










































#------------------------------------------------------------------

class Options:
    default_options = {
            'port': 22,
            'host': 'localhost',
            'username': None,
            'password': None,
            'debug': False,
            }
    def __init__(self, **kwargs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)

    def __getitem__(self, key):
        return self.options[key]

#a=dict(host=2222, password='titi')
#print(type(a))
#x= Options(a)
#print(x['port'])


import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)

class Polygon:
    def __init__(self, points = []):
        self.vertices = []
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)
            self.vertices.append(point)

    def add_point(self, point):
        self.vertices.append((point))

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter

square = Polygon()
square.add_point(Point(1,1))
square.add_point(Point(1,2))
square.add_point(Point(2,2))
square.add_point(Point(2,1))
t= square.perimeter()
#print(t)