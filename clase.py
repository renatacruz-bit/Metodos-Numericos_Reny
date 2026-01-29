import numpy as np
import matplotlib.pyplot as plt

m=np.linspace(0, 15, 100)

error=0.12500e-5*3**m
plt.figure()
plt.plot(m, error)
plt.xlabel("m")
plt.ylabel(r"$p_m-\ hat{p}_m$")
plt.title("grafica de error por redondeo")
plt.grid() #enmallado
plt.show()




































