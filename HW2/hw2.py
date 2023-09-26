def q1(roots):
    # Finding the roots of the polynomia
    poly = [1]
    for root in roots:
        new_poly = [0] * (len(poly) + 1)
        for i in range(len(poly)):
            new_poly[i] += poly[i]
            new_poly[i + 1] -= root * poly[i]
        poly = new_poly

    return poly

#print(q1([2,3]))


def q2(coefficients):
    # Step (a): Find the factors for k
    k = coefficients[-1]
    lst = []
    for i in range(1, abs(k) + 1):
        # Check if k is evenly divisible by i
        if k % i == 0:
            # If it is, add i to the list lst
            lst.append(i)

    # Initialize a list to store the unique roots
    unique_roots = []

    # Step (b): checking if the result is zero or not if it's zero then that is the factor
    for c in lst:
        result = 0
        for coef in coefficients:
            result = result * c + coef

        if result == 0:
            unique_roots.append(c)
        else:
            new_lst = []
            for x in lst:
                if x - c != 0 and result % (x - c) == 0:
                    new_lst.append(x)
            lst = new_lst

    return unique_roots

# Test cases
print(q2([1, -5, 6]))
print(q2([1, -12, 47, -60]))

