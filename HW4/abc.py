class Exp:
    def _str_(self):
        raise Exception('unsupported')

    def deriv(self, x):
        raise Exception('unsupported')

    def simp(self):
        return self

    def simplify(self):
        return self


class Const(Exp):
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return str(self.n)

    def __add__(self, other):
        if isinstance(other, Const):
            return Const(self.n + other.n)
        else:
            return Plus(self, other)

    def __mul__(self, other):
        if isinstance(other, Const):
            return Const(self.n * other.n)
        else:
            return Times(self, other)

    def __pow__(self, n):
        return Pow(self, n)

    def deriv(self, x):
        return Const(0)


class Var(Exp):
    def __init__(self, v):
        self.v = v

    def __str__(self):
        return self.v

    def __add__(self, other):
        return Plus(self, other)

    def __mul__(self, other):
        return Times(self, other)

    def __pow__(self, n):
        return Pow(self, n)

    def deriv(self, x):
        if self.v == x:
            return Const(1)
        else:
            return Const(0)


class Plus(Exp):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def __str__(self):
        return f"({self.e1} + {self.e2})"

    def deriv(self, x):
        return Plus(self.e1.deriv(x) , self.e2.deriv(x))

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
        return f"({self.e1} * {self.e2})"

    def deriv(self, x):
        # Apply the product rule: d/dx (e1 * e2) = e1 * e2' + e1' * e2
        return Plus(Times(self.e1, self.e2.deriv(x)), Times(self.e1.deriv(x), self.e2))

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
        return f"({self.e} ** {self.n})"

    def deriv(self, x):
        # Apply the power rule: d/dx (e^n) = n * (e^(n-1)) * e'
        return Times(Times(Const(self.n), Pow(self.e, Const(self.n - 1))), self.e.deriv(x))

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


# example usage
x = Var('x')
e = Times(Times(x, Var('y')), Plus(x, Const(3)))
e1 = Pow(x, 4)
e2 = Pow(Plus(x, Const(0)), 2)

print(e)
print(e1)
print(e2)

print(e.deriv('x'))  # ((1 * y) * (x + 3)) + ((x * y) * 1)
print(e1.deriv('x'))  # (4 * (x ** 3)*1)

print(e.deriv('x').simplify())  # (y * (x + 3)) + (x * y)
print(e1.deriv('x').simplify())  # (4 * (x ** 3))

print(e2.simplify()) #(x ** 2)