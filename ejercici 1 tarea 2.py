import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0, 15, 100)
error=0.3334e-4*x

plt.figure()
plt.plot(x, error)
plt.xlabel("x")
plt.ylabel(r"$p_x-\hat{p}_x$")
plt.title("Grafica de error por redondeo")
plt.grid() #enmallado
plt.show()