#X = 90

#def test (a = 0, b = 12 , c=67):
#    X=88
#    print(a, b, c)
#    print ("x internal", X)

#test (1, 2, 3)
#test(1, c=456)
#print(X)

def multiply(x,y):
    print ( x * y)

print (multiply(5,4))

def multi(*args):
    z = 1
    for num in args:
        z *= num
    print (z)

multi(4,'a',5)
multi(4,5,4,5,6,7,8)

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a="3", b="5", c="56")







