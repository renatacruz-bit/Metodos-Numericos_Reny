import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5, 5, 100)
y=np.exp(x)

plt.plot(x, y)
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Grafica")
plt.grid() #enmallado

plt.savefig("exponencial.png,  dpi=300")
plt.show()


