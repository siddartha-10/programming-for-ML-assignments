#Q1
def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result =result * i
        print('*'.join(str(j) for j in range(1, i + 1)), '=', result)
        i += 1
    return result
factorial_result = factorial(10)


#Q2
def deriv(polynomial, n):
    if n == 0:
        return polynomial
    if n >= len(polynomial):
        return []
    derivative = []
    for i in range(len(polynomial)-1):
        derivative.append(polynomial[i]*(len(polynomial)-i-1))
    return deriv(derivative, n-1)

print(deriv([2,-4,4], 1))
print(deriv([2,-4,4],2))
print(deriv([2,-4,4],3))

#Q3

# the main problem with the given method is that since we are iterating and also removing elements
# from the same list there maybe skiping of elements
# correct solution
def remove(l1, l2):
    result = [x for x in l1 if x not in l2]
    return result
# instead of removing we will add it to a new list.

#Q4
# class Exp:
#     def eval(self, ctx): raise Exception('unsupported')

class Let(Exp):
    def __init__(self, x, e1, e2):
        self.x = x
        self.e1 = e1
        self.e2 = e2

    def eval(self, ctx):
        v = self.e1.eval(ctx)
        ctx[self.x] = v
        return self.e2.eval(ctx)

#Q5
from typing import Dict
class Exp:
    def eval(self, ctx: Dict[str, int]) -> int:
        raise Exception("unsupported")

    def deriv(self, x: str) -> 'Exp':
        raise Exception("unsupported")


class Const(Exp):
    def __init__(self, n: int) -> None:
        self.n: int = n

    def eval(self, ctx: Dict[str, int]) -> int:
        return self.n

    def deriv(self, x: str) -> 'Const':
        return Const(0)


class Var(Exp):
    def __init__(self, v: str) -> None:
        self.v: str = v

    def eval(self, ctx: Dict[str, int]) -> int:
        return ctx[self.v]

    def deriv(self, x: str) -> Exp:
        if self.v == x:
            return Const(1)
        else:
            return Const(0)


class Plus(Exp):
    def __init__(self, e1: Exp, e2: Exp) -> None:
        self.e1: Exp = e1
        self.e2: Exp = e2

    def eval(self, ctx: Dict[str, int]) -> int:
        return self.e1.eval(ctx) + self.e2.eval(ctx)

    def deriv(self, x: str) -> Exp:
        return Plus(self.e1.deriv(x), self.e2.deriv(x))


class Times(Exp):
    def __init__(self, e1: Exp, e2: Exp) -> None:
        self.e1: Exp = e1
        self.e2: Exp = e2

    def eval(self, ctx: Dict[str, int]) -> int:
        return self.e1.eval(ctx) * self.e2.eval(ctx)

    def deriv(self, x: str) -> Exp:
        return Plus(Times(self.e1.deriv(x), self.e2), Times(self.e1, self.e2.deriv(x)))

class Pow(Exp):
    def __init__(self, e: Exp, n: int) -> None:
        self.e: Exp = e
        self.n: int = n

    def eval(self, ctx: Dict[str, int]) -> int:
        return self.e.eval(ctx) ** self.n

    def deriv(self, x: str) -> Exp:
        return Times(Times(Const(self.n) , Pow(self.e, self.n - 1)), self.e.deriv(x))
