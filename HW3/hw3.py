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

def toString(e):
    tag, value = e
    if tag == 'const':
        return str(value)
    elif tag == 'var':
        return value
    elif tag == 'plus':
        return f'({toString(value[0])} + {toString(value[1])})'
    elif tag == 'times':
        return f'({toString(value[0])} * {toString(value[1])})'
    elif tag == 'exp':
        return f'({toString(value[0])}^{value[1]})'

def deriv(u, x):
    tag, value = u
    if tag == 'const':
        return const(0)
    elif tag == 'var':
        if value == x:
            return const(1)
        else:
            return const(0)
    elif tag == 'plus':
        du1 = deriv(value[0], x)
        du2 = deriv(value[1], x)
        return simplify(plus(du1, du2))
    elif tag == 'times':
        du1 = deriv(value[0], x)
        du2 = deriv(value[1], x)
        return simplify(plus(times(du1, value[1]), times(value[0], du2)))
    elif tag == 'exp':
        du = deriv(value[0], x)
        return simplify(times(times(const(value[1]), exp(value[0], value[1] - 1)), du))

def simplify(e):
    tag, value = e
    if tag == 'plus':
        value[0] = simplify(value[0])
        value[1] = simplify(value[1])
        if value[0][0] == 'const' and value[0][1] == 0:
            return value[1]
        elif value[1][0] == 'const' and value[1][1] == 0:
            return value[0]
        return e
    elif tag == 'times':
        value[0] = simplify(value[0])
        value[1] = simplify(value[1])
        if value[0][0] == 'const' and value[0][1] == 0:
            return const(0)
        elif value[1][0] == 'const' and value[1][1] == 0:
            return const(0)
        elif value[0][0] == 'const' and value[0][1] == 1:
            return value[1]
        elif value[1][0] == 'const' and value[1][1] == 1:
            return value[0]
        return e
    elif tag == 'exp':
        value[0] = simplify(value[0])
        if value[0][0] == 'const' and value[0][1] == 0:
            return const(1)
        elif value[0][0] == 'const' and value[0][1] == 1:
            return const(1)
        return e
    return e

# Example usage:
e = times(times(var('x'), var('y')), plus(var('x'), const(3)))
e1 = exp(var('x'), 4)

print(toString(e))  # Output: "((x * y) * (x + 3))"
print(toString(e1)) # Output: "(x^4)"

derivative_e = deriv(e, 'x')
derivative_e1 = deriv(e1, 'x')

print(toString(derivative_e))  # Output: "(((1 * y) + (x * 0)) * (x + 3)) + ((x * y) * (1 + 0))"
print(toString(derivative_e1)) # Output: "(4 * (x^3))"
