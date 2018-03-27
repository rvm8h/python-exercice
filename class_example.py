
class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

x = FirstClass()
y = FirstClass()

x.setdata("Thomas")
y.setdata(3.1415)

x.display()
y.display()

<<<<<<< HEAD

class SecondClass(FirstClass):
    def display(self):
        print("current value : {}".format(self.data))

z = SecondClass()
=======
class SecondClass(FirstClass):
    def display(self):
        print("Current value : {}".format(self.data))


z = SecondClass()

>>>>>>> 6e539344271fa91285870851b917bccea507f2ba
z.setdata(456)
z.display()

class ThirdClass(SecondClass):
    def __init__(self,value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[ThirdClass : {} ]'.format(self.data)
    def mul(self,other):
        self.data *= other

a = ThirdClass('abc')
a.display()
<<<<<<< HEAD
print(a)

b = a + 'xyz'
b.display()
print(b)
=======
# Le print correspond à str
print(a)

# Le + correspond à add
b = a + 'xyz'
b.display()
print(b)

>>>>>>> 6e539344271fa91285870851b917bccea507f2ba
