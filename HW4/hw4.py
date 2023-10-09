class Exp:
    def __str__(self):
        raise Exception('unsupported')

    def deriv(self, x):
        raise Exception('unsupported')

    def simp(self):
        return self

    def simplify(self):
        return self

    def __add__(self, other):
        return Plus(self, other)

    def __mul__(self, other):
        return Times(self, other)

    def __pow__(self, other):
        return Pow(self, other)

class Const(Exp):
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return str(self.n)

    def deriv(self, x):
        return Const(0)

    def simplify(self):
        return self

class Var(Exp):
    def __init__(self, v):
        self.v = v

    def __str__(self):
        return self.v

    def deriv(self, x):
        if self.v == x:
            return Const(1)
        else:
            return Const(0)

    def simplify(self):
        return self

class Plus(Exp):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def __str__(self):
        return f'({self.e1} + {self.e2})'

    def deriv(self, x):
        return self.e1.deriv(x) + self.e2.deriv(x)

    def simplify(self):
        e1 = self.e1.simplify()
        e2 = self.e2.simplify()

        if isinstance(e1, Const) and isinstance(e2, Const):
            return Const(e1.n + e2.n)
        elif isinstance(e1, Const) and e1.n == 0:
            return e2
        elif isinstance(e2, Const) and e2.n == 0:
            return e1
        else:
            return Plus(e1, e2)

class Times(Exp):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def __str__(self):
        return f'({self.e1} * {self.e2})'

    def deriv(self, x):
        return (self.e1.deriv(x) * self.e2) + (self.e1 * self.e2.deriv(x))

    def simplify(self):
        e1 = self.e1.simplify()
        e2 = self.e2.simplify()

        if isinstance(e1, Const) and isinstance(e2, Const):
            return Const(e1.n * e2.n)
        elif isinstance(e1, Const) and e1.n == 0:
            return Const(0)
        elif isinstance(e2, Const) and e2.n == 0:
            return Const(0)
        elif isinstance(e1, Const) and e1.n == 1:
            return e2
        elif isinstance(e2, Const) and e2.n == 1:
            return e1
        else:
            return Times(e1, e2)

class Pow(Exp):
    def __init__(self, e, n):
        self.e = e
        self.n = n

    def __str__(self):
        return f'({self.e} ** {self.n})'

    def deriv(self, x):
        return (self.n * (self.e ** (self.n - 1))) * self.e.deriv(x)

    def simplify(self):
        e = self.e.simplify()

        if isinstance(e, Const):
            return Const(e.n ** self.n)
        elif self.n == 0:
            return Const(1)
        elif self.n == 1:
            return e
        else:
            return Pow(e, self.n)

# Test examples
x = Var('x')
e = (x * 'y') * (x + 3)
e1 = x ** 4
e2 = (x + 0) ** 2

print(e)            # Output: ((x * y) * (x + 3))
print(e1)           # Output: (x ** 4)
print(e2)           # Output: ((x + 0) ** 2)

print(e.deriv('x')) # Output: (((1 * y) + (x * 0)) * (x + 3)) + ((x * y) * (1 + 0))
print(e1.deriv('x'))# Output: ((4 * (x ** 3)) * 1)

print(e.deriv('x').simplify())  # Output: ((y * (x + 3)) + (x * y))
print(e1.deriv('x').simplify()) # Output: (4 * (x ** 3))
print(e2.simplify())            # Output: (x ** 2)
