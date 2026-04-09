import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from sympy  import symbols, lambdify

x=sp.symbols('x')
expr=1/x
x_0=2
x_1=2.5
x_2=4

l0=((x-x_1)/(x_0-x_1))*((x-x_2)/(x_0-x_2))
l1=((x-x_0)/(x_1-x_0))*((x-x_2)/(x_1-x_2))
l2=((x-x_0)/(x_2-x_0))*((x-x_1)/(x_2-x_1))


resultado=sp.expand(expr)
print(resultado)

f=lambdify(x, expr, 'numpy')

xs=np.linspace(0.1, 10, 100 )
ys=f(xs)

plt.plot(xs, ys)
plt.grid()
plt.show()