# not my code btw
import math

a = 1
b = 2
c = 0


def root():
    global a, b, c
    try:
        d = b ** 2 - 4 * a * c
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        if x1 == x2:
            raise (UserWarning('Only one root!'))
    except ValueError:  # Negative value in sqrt causes ValueError
        return ()
    except UserWarning:
        return (x1)
    else:
        return (x1, x2)
    finally:
        # coeffecient are very secret numbers that must be deleted!
        del a, b, c  # the del command erases the numbers from memmory


print(root())