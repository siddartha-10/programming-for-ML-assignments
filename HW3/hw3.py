def const(n):
    return ('const', n)

def var(s):
    return ('var', s)

def plus(e1, e2):
    return ('plus', (e1, e2))

def times(e1, e2):
    return ('times', (e1, e2))

def exp(e, n):
    return ('exp', (e, n))

def toString(expr):
    a, b = expr
    if a == 'const':
        return str(b)
    elif a == 'var':
        return b
    elif a == 'plus':
        e1, e2 = b
        return f"({toString(e1)} + {toString(e2)})"
    elif a == 'times':
        e1, e2 = b
        return f"({toString(e1)} * {toString(e2)})"
    elif a == 'exp':
        e, n = b
        return f"({toString(e)}^{n})"


def deriv(expr, x):
    a, b = expr
    # Here this condition is the base and since derivative of const is zero
    if a == 'const':
        return const(0)

    # If the value of b is x then return 1 else again return 0
    elif a == 'var':
        return const(1) if b == x else const(0)

    # I am trying to use the sum rule of this and also calling the deriv function recursively
    elif a == 'plus':
        e1, e2 = b
        du1 = deriv(e1, x)
        du2 = deriv(e2, x)
        return plus(du1, du2)

    # I am trying to use the product rule of this and also calling the deriv function recursively
    elif a == 'times':
        e1, e2 = b
        du1 = deriv(e1, x)
        du2 = deriv(e2, x)
        return plus(times(du1, e2), times(e1, du2))

    # I am trying to use the power rule of this and also calling the deriv function recursively
    elif a == 'exp':
        e, n = b
        du = deriv(e, x)
        return times(const(n), times(exp(e, n - 1), du))



def simplify(expr):
    a, b = expr
    if a == 'plus':
        e1, e2 = b
        se1 = simplify(e1)
        se2 = simplify(e2)
        if se1 == const(0):
            return se2
        elif se2 == const(0):
            return se1
        else:
            return plus(se1, se2)
    elif a == 'times':
        e1, e2 = b
        se1 = simplify(e1)
        se2 = simplify(e2)
        if se1 == const(0) or se2 == const(0):
            return const(0)
        elif se1 == const(1):
            return se2
        elif se2 == const(1):
            return se1
        else:
            return times(se1, se2)
    else:
        return expr
# The above simple code when the expression is having plus it will look if there are any constants or not if there is then it will
# remove the constants and returns the output similar to when there is times. If there is no plus or times in the expression then
# it will return the original expression itself.

e = times(times(var('x'), var('y')), plus(var('x'), const(3)))
e1 = exp(var('x'), 4)

print(toString(e))
print(toString(e1))


print(toString(deriv(e, 'x')))
print(toString(deriv(e1, 'x')))

print(toString(simplify(deriv(e, 'x'))))
print(toString(simplify(deriv(e1, 'x'))))
