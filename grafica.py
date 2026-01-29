#grafica la funcion x^2
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5, 5, 100)
y=x**2

plt.plot(x, y)
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Grafica de f(x)=x^2")
plt.grid() #enmallado
plt.show()
