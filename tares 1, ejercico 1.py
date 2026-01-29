import math
import matplotlib.pyplot as plt

x=0.5
valor_exacto=math.pi
sum=0
n_valores=[]
error_relativo=[]

print("="*68)
print(f"{'n':^10} | {'aprox pi':^14} | {'error Abs':^14} | {'Error rel':^14}")
print("="*68)


sum=0
for n in range(20):
        sum=sum+x**n/math.factorial(n)

        error_abs=abs(valor_exacto-sum)
        error_rel=error_abs/valor_exacto

        n_valores.append(n)
        error_relativo.append(error_rel)
        
        print(f"{'n':^10} | {'aprox pi':^14.8f} | {'error Abs':^14.8f} | {'Error rel':^14.8f}")

        if error_rel<0.5e-11:
            break
print("0"*68)

plt.figure()
plt.plot(n_valores, error_relativo, marker='o')
plt.xlabel("n(grado del polinomio)")
plt.ylabel("error relativo")
plt.title("convergencia de la serie de taylor e^x en 0.5")
plt.show()



  