import numpy as np
import matplotlib.pyplot as plt


def h(x):
    return 1/(np.sqrt(2*np.pi))*np.exp(-0.5*x**2)


x = np.linspace(-4, 4, 41)
y = np.array([h(i) for i in x])

print(x)
print(y)

plt.plot(x, y)
plt.savefig('h.pdf')
