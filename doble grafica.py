import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5, 5, 100)

plt.plot(x, x+1, label="x+1")
plt.plot(x, x**2, label="x^2")

plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Dos graficas")
plt.grid() #enmallado
plt.show()
