def q1(roots):
  for root in roots:
    polynomial = [a - b * root for a, b in zip(polynomial, polynomial[1:])]

  return polynomial



def q2(polynomial):
  """Finds the unique roots of a polynomial using the remainder theorem.

  Args:
    polynomial: A list of integer coefficients of the polynomial, starting with the
      most significant term.

  Returns:
    A list of integer roots of the polynomial.
  """

  # Initialize the list of roots.
  roots = []

  # Iterate over the factors of the constant term and check if any of them is a
  # root of the polynomial.
  constant_term = polynomial[-1]
  factors = []
  for i in range(1, abs(constant_term) + 1):
    if constant_term % i == 0:
      factors.append(i)
      factors.append(-i)

  for factor in factors:
    if polynomial(factor) == 0:
      roots.append(factor)
      # Remove the factor from the list of factors so that it is not checked
      # again.
      factors.remove(factor)
      # Reduce the degree of the polynomial by dividing by the linear factor
      # (x - factor).
      polynomial = polynomial[:-1]
      polynomial = [a - b * factor for a, b in zip(polynomial, polynomial[1:])]

  # If the polynomial is not constant, then it has no more roots.
  if polynomial[-1] != 0:
    return roots

  # Otherwise, all the remaining factors of the constant term are roots of the
  # polynomial.
  roots.extend(factors)
  return roots
