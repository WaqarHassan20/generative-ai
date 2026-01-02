# Method Resolution Order (MRO) in Python

class A:
    label = "A: Base class"


class B:
    # pass
    label = "B: ginger blends"


class C:
    # pass
    label = "C: lemon blends"


class D(B, C):
    pass


cup = D()
print(cup.label)
print(D.mro())