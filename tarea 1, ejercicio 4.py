import numpy as np
import matplotlib.pyplot as plt

def taylor_log(x, n):
    sum=0

    for k in range(1, n+1):
        sum=sum+((-1)**(k+1))*(x-1)**k/k
    
    return sum

x=np.linspace(0.1, 2, 100)

plt.figure(figsize=(8, 6))
plt.plot(x, np.log(x), label=r"log(x)", linewidth=1)

for n in [1, 2, 4, 8, 16]:
    plt.plot(x, taylor_log(x, n), label=f"taylor de grado {n}", linewidth=3)

plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Grafica de log(x)")
plt.grid() #enmallado
plt.legend()
plt.savefig("logaridmo.png",  dpi=300)
plt.show()