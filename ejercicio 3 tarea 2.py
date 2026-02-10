import math
import matplotlib.pyplot as plt

x=0.5
valor_exacto=math.exp(x)

sum=0
n_valores=[]
error_relativo=[]

print("="*68)
print(f"{'n':^10} | {'aprox e^x':^14} | {'error Abs':^14} | {'Error rel':^14}")
print("="*68)


sum=0
for n in range(20):
        sum=sum+x**n/math.factorial(n)

        error_abs=abs(valor_exacto-sum)
        error_rel=error_abs/valor_exacto

        n_valores.append(n)
        error_relativo.append(error_rel)
        
        print(f"{n:^5.8f} | {sum:^14.8f} | {error_abs:^14.8f} | {error_rel:^14.8f}")

        if error_rel<0.1e-1:
            break
print("="*68)

print(valor_exacto)
print("="*68)

plt.figure()
plt.plot(n_valores, error_relativo, marker='o')
plt.xlabel("n(grado del polinomio)")
plt.ylabel("error relativo")
plt.title("convergencia de la serie de taylor e^x en 0.5")
plt.show()



  