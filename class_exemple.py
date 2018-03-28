class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)
x = FirstClass()
y=FirstClass()
x.setdata("Thomas")
y.setdata(3.1415)
x.display()
y.display()

class SecondClass(FirstClass):
    def display(self):
        print("current values : ()".format(self.data))
z = SecondClass()
z.setdata(456)

# creation d'une classe
class FirstClass:
    def setdata(self, value):
        self.data  = value

    def display(self):
        print(self.data)


x = FirstClass()
y = FirstClass()

x.setdata("Thomas")
y.setdata(3.1415)

x.display()
y.display()

# heritage


class SecondClass(FirstClass):
    # overloading display
    def display(self):
        print("current value: {}".format(self.data))


z = SecondClass()
z.setdata(444)

z.display()


class ThirdClass(SecondClass):

    def __init__(self,value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data+other)
    def __str__(self):
        return '[ThirdClass : {} ]'.format(self.data)
    def _mul(self, other):
          self.data*= other

    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass: {} ]'.format(self.data)

    def mul(self, other):
        self.data = other



a = ThirdClass('abc')
a.display()
print(a)

b = a + 'xyz'
b.display()

print(b)

print(b)


