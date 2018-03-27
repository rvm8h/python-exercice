

class Point:
    def __init__(self, coordx=0, coordy=0):
        self.coordx = coordx
        self.coordy = coordy
    def __str__(self):
        return '[coordx : {}, coordy : {}]'.format(self.coordx, self.coordy)
    def display(self):
        print('Point : [coordx :', self.coordx, ', coordy :', self.coordy, ']')


p = Point(1,9)
print(p)
p.display()

class Segment:
    def __init__(self, coordxorig=0, coordyorig=0, coordxextr=0, coordyextr=0):
        self.orig = Point(coordxorig, coordyorig)
        self.extr = Point(coordxextr, coordyextr)
    def __str__(self):
        return '[{} , {}]'.format(self.orig, self.extr)
    def display(self):
        print('Segment : ', self.orig.__str__(), ',', self.extr.__str__())


seg = Segment(1, 2, 5, 0)
print(seg)
seg.display()

