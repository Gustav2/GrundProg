def polynomial(x: int, p: dict):
    """Return the value of a polynomial at x."""
    running_sum = 0
    for i in p:
        running_sum += p[i] * x ** i
    return running_sum


p1 = {3: 1, 2: -2, 1: -1, 0: 2}
print(polynomial(0, p1))

p2 = {10: 2, 0: -48}
print(polynomial(2, p2))