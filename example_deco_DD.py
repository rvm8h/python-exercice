import time


def deco(func):
    def inner():
        print("running inner")
        print(func.__name__)
    return inner

# La fonction target devient le parametre de la fonction deco


@deco
def target():
    print("running target")


target()
print(target)

registry = []


def register(func):
    print("running {}".format(func))
    registry.append(func)

    return func


@register
def f1():
    print("running f1")


@register
def f2():
    print("running f2")


def f3():
    print("running f3")


def main():
    print("running main")
    print("registry ->", registry)
    f1()
    f2()
    f3()


if __name__ == "__main__":
    main()

#######################################


def clock(func):
    def clocked(*args):
        t0      = time.perf_counter()
        result  = func(*args)
        elapsed = time.perf_counter() - t0
        name    = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


if __name__ == "__main__":
    main()
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))
