def deco(funct):
    def inner():
        print("running inner")
        print(funct.__name__)
    return inner

@deco
def target() :
    print("running target")

target()
print(target)

#deco(target)
#target = decorator(target)


registry = []

def register(funct):
    print("running register {}".format(funct))
    registry.append(funct)
    return funct

@register
def f1():
    print("running F1")

@register
def f2():
    print("running F2")


def f3():
    print("running F3")

def main():
    print("running main")
    print("registry =>", registry)
    f1()
    f2()
    f3()

if __name__ == "__main__":
    main()