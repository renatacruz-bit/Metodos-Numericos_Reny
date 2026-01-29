import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10, 10, 100)
plt.plot(x, x**3,
         color="pink",
         linestyle="--",
         linewidth=3,
         label="x^3"
         )

plt.plot(x, np.cos(x),
         color="magenta",
         linestyle=":",
         linewidth=4,
         label="cosx")

plt.plot(x, np.exp(-x),
         color="orange",
         linestyle="-",
         linewidth=2,
         label="e^(-x)")


plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Grafica de f(x)=x^2")
plt.grid() #enmallado
plt.show()
