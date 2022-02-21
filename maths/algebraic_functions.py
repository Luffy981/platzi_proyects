#!/usr/bin/env python3
# librarie to graphics
import matplotlib.pyplot as plt
# librarie to use vectors and maths
import numpy as np

# Desplazamientos verticales y horizontales
# Siendo  c  una constante mayor que cero, entonces la gráfica:
# y=f(x)+c  se desplaza  c  unidades hacia arriba.
# y=f(x)−c  se desplaza  c  unidades hacia abajo.
# y=f(x−c)  se desplaza  c  unidades hacia la derecha.
# y=f(x+c)  se desplaza  c  unidades hacia la izquierda.

# Alargamientos y compresiones
# Siendo  c  una constante mayor que cero, entonces la gráfica:
#
# y=c⋅f(x)  alarga la gráfica verticalmente en un factor de  c .
# y=1c⋅f(x)  comprime la gráfica verticalmente en un factor de  c .
# y=f(c⋅x)  comprime la gráfica horizontelmente en un factor de  c .
# y=f(1c⋅x)  alarga la gráfica horizontelmente en un factor de  c .

# Reflexiones
# y=−f(x)  refleja la gráfica respecto al eje x.
# y=f(−x)  refleja la gráfica respecto al eje y.
N = 100
m = -1
b = 3


def f(x):
    """Linear function"""
    return m * x + b


x = np.linspace(-10, 10, num=N)
y = f(x)
print(y)
print(y.shape)
fig, ax = plt.subplots()
ax.plot(x, y, color='red', linewidth=3, label='linear')
ax.grid()
plt.legend()
plt.show()


def f(x):
    """Polinomial function"""
    return(2 * x**7) - (x**4) + (3 * x**2) + 4


x = np.linspace(-10, 10, num=N)
y = f(x)
plt.plot(x, y, color='red', linewidth=3, label='Polinomial')
plt.grid()
plt.legend()
plt.show()


def f(x):
    """Trigonometric function"""
    return np.cos(x)


x = np.linspace(-10, 10, num=N)
y = f(x)
plt.plot(x, y, color='red', linewidth=3, label='Trigonometric')
plt.grid()
plt.legend()
plt.show()


def f(x):
    """Exponential function"""
    return np.exp(x)


x = np.linspace(-10, 10, num=N)
y = f(x)
plt.plot(x, y, color='red', linewidth=3, label='Exponential')
plt.grid()
plt.legend()
plt.show()


def f(x):
    """Logarithmic function"""
    return np.log2(x)


x = np.linspace(0.01, 256, num=1000)
y = f(x)
plt.plot(x, y, color='red', linewidth=3, label='Logarithmic')
plt.grid()
plt.legend()
plt.show()


def H(x):
    Y = np.zeros(len(x))
    for idx, x in enumerate(x):
        if x >= 0:
            Y[idx] = 1
    return Y


N = 1000
x = np.linspace(-10, 10, num=N)
y = H(x)
plt.plot(x, y, color='red', linewidth=3, label='Sectioned')
plt.grid()
plt.legend()
plt.show()


