import math 
import numpy as np
import matplotlib.pyplot as plt

def taylor_exp(x, n):
    sum=0
    
    for k in range(n+1):
        sum=sum+x**k/math.factorial(k)
        
    return sum

x=np.linspace(-5, 5, 100)

plt.figure(figsize=(8, 6))

plt.plot(x, np.exp(x), label=r"e^x", linewidth=1)

for n in [1, 2, 4, 8]:
    plt.plot(x, taylor_exp(x, n), label=f"taylor de grado {n}", linewidth=1)
    
plt.xlabel("x")
plt.ylabel("y")
plt.title("grafica de la exponencial")
plt.legend()
plt.grid()
plt.show()