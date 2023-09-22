def q1(roots):
    polynomial = [1]

    for root in roots:
        new_polynomial = [0] * (len(polynomial) + 1)
        for i in range(len(polynomial)):
            new_polynomial[i] += polynomial[i]
            new_polynomial[i + 1] -= root * polynomial[i]
        polynomial = new_polynomial

    return polynomial


# Test cases
print(q1([2, 3])) 
