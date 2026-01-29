import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5, 5, 100)
plt.plot(x, 2*x+1,
         color="red",
         linestyle="--",
         linewidth=3,
         label="2x+1"
         )

plt.plot(x, x**2,
         color="green",
         linestyle="-.",
         linewidth=1,
         label="x^2")


plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Grafica de f(x)=x^2")
plt.grid() #enmallado
plt.show()
