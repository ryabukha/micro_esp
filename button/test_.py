a = 1


def f():
    print("insade f(): ", a)


def g(a=5):
    # a = 2
    print("insade g(): ", a)


def h():
    global a
    a = 3
    print("insade h(): ", a)


print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)
i =+ 1
print(i)
