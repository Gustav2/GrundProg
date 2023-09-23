def find_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)

    return x1, x2