import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5, 5, 100)

plt.plot(x, 2*x+1,
         color="blue",
         linestyle="-.",
         linewidth=2,
         label="2x+1"
         )

plt.plot(x, x**2,
         color="pink",
         linestyle=":",
         linewidth=3,
         label="x^2"
         )


plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Grafica ")
plt.grid() #enmallado
plt.show()
