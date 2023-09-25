import numpy as np
import matplotlib.pyplot as plt

# 5.b
def polynomial(x, coefficients):
    return sum([coefficients[i] * x**i for i in range(len(coefficients))])


coefs = np.array([6, -8, 2, -3, 1])

print(polynomial(1, coefs))


# 5.c
def np_polynomial(x, coefficients):
    y = np.zeros(len(x))
    for i in range(len(coefficients)):
        y += coefficients[i] * x**i
    return y


x = np.linspace(0, 3, 7)
print("np_polynomial")
print(np_polynomial(x, coefs))


# 5.e
def np_poly_no_loops(x, coefficients):
    x = np.transpose(np.atleast_2d(x))
    x_mat = np.tile(x, (1, len(coefficients)))

    coef_mat = np.tile(coefficients, (len(x), 1))

    y = np.sum(coef_mat * x_mat**np.arange(len(coefficients)), axis=1)
    return y


print("np_poly_no_loops")
print(np_poly_no_loops(x, coefs))


# 5.d
def f(x):
    return 6 - 8*x + 2*x**2 - 3*x**3 + x**4


# plot function in [0, 3.2]
x = np.linspace(0, 3.2, 100)
plt.plot(x, f(x))
plt.show()

