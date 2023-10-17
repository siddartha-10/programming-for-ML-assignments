def prime():
    primes = []
    num = 2
    while True:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
            yield num
        num += 1
p = prime()
count = 0
for _ in range(10):
    count += 1
    print(next(p))

for _ in range(10):
    count += 1
    print(next(p))

class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __iter__(self):
        degree = len(self.coeffs) - 1
        for coeff in self.coeffs:
            yield coeff, degree
            degree -= 1

    def __str__(self):
        if not self.coeffs:
            return "0"
        terms = []
        for coeff, degree in self:
            if coeff == 0:
                continue
            if degree == 0:
                terms.append(str(coeff))
            elif degree == 1:
                terms.append(f"{coeff}x")
            else:
                terms.append(f"{coeff}x^{degree}")
        return join_new(terms)
    def __add__(self, other):
        max_degree = max(len(self.coeffs), len(other.coeffs))
        coeffs_self = [0] * (max_degree - len(self.coeffs)) + self.coeffs
        coeffs_other = [0] * (max_degree - len(other.coeffs)) + other.coeffs

        result_coeffs = [coeffs_self[i] + coeffs_other[i] for i in range(max_degree)]

        return Polynomial(result_coeffs)

    def __mul__(self, other):
        degree_self = len(self.coeffs) - 1
        degree_other = len(other.coeffs) - 1
        result = degree_self + degree_other
        result_coeffs = [0] * (result + 1)

        for i in range(degree_self + 1):
            for j in range(degree_other + 1):
                result_coeffs[i + j] += self.coeffs[i] * other.coeffs[j]

        return Polynomial(result_coeffs)

    def __call__(self, x):
        result = 0
        for coeff, degree in self:
            result += coeff * (x ** degree)
        return result

def join_new(terms):
    str = ''
    for i in range(0, len(terms)):
        if(i == 0):
            str += terms[i]
        else:
            if(terms[i][0] == '-'):
                str +=  terms[i]
            else:
                str += '+' + terms[i]
    return str



p1 = Polynomial([3, 2, -1]) # 3x^2 + 2x - 1
p2 = Polynomial([-1, 1]) # -x + 1
p3 = Polynomial([0,0,-4])
p4 = Polynomial([0])

for c,d in p1:
    print(c,d)

print(p1)
print(p2)
print(p3)
print(p4)

p1 = Polynomial([3, 2, -1]) # 3x^2 + 2x - 1
p2 = Polynomial([-1, 1]) # -x + 1
print(p1+p2)
print(p1*p2)
print(p1(2))