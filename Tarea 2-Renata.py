#ejercicio 1

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0, 15, 100)
error=0.3334e-4*x

plt.figure()
plt.plot(x, error)
plt.xlabel("x")
plt.ylabel(r"$p_x-\hat{p}_x$")
plt.title("Grafica de Error por Redondeo")
plt.grid() #enmallado
plt.show()

#Ejercicoio 2

import math

def sucesion_Euler(n):
    sucesion=0
    for k in range(1,n+1):
        sucesion += 1/k
    return sucesion - math.log(n)

Error_real=0.5772156649
Tolerancia=1e-4
n=0

print("="*80)
print(f"{'n':^10} | {'Aprox Euler':^22} | {'Error Abs':^18} | {'Error Rel':^18}")
print("="*80)

while True:
    n += 1
    Aproximacion=sucesion_Euler(n)
    Error_Absoluto=abs(Error_real-Aproximacion)
    if Error_Absoluto < Tolerancia:
        break
    print(f"{n:^10} | {Aproximacion:^19.8f} | {Error_Absoluto:^14.8f} | {Error_real:^14.8f}")

print("="*66)
print("Valor real: ", Error_real)
print("Error Absoluto: ", Error_Absoluto)
print("Aproximacion: ", Aproximacion)
print("Valor de n: ", n)
print("="*66)


#Ejercicios 3

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


#Ejercicio 4
print("Perdon, no pude hacerlo")
print("que burrra soy, pongame 0")

print("="*65)
print("\t #Ejercico 4")
print("="*65)

def p_9(x):
    sum = 0
    for n in range(10):
        sum += (x**n)/math.factorial(n)
    return sum

cota = math.e / math.factorial(10)
to = 1e-6
max_error = 0
max_error_x = 0
num_p = 101

for i in range(num_p):
    x = -1 + 2 * i / (num_p - 1)
    val_exacto = math.exp(x)
    aprox = p_9(x)
    error_abs = abs(val_exacto - aprox)
    if error_abs > max_error:
        max_error = error_abs
        max_error_x = x

print("-"*65)
print(f"Verificacion numerica en {num_p} puntos para x en [-1, 1]")
print(f"Maximo error encontrado en {max_error} en x= {max_error_x}")
print("-"*65)
print("Comparacion con la cota teorica")
print(f"Cota teorica: {cota}")
print(f"Error maximo (|e^x - p_9(x)|): {max_error}")
print("-"*65)

if cota <= to and max_error <= to:
    print("Por lo tanto se cumple")
    print("Ya que la cota teorica es menor ")
    print("="*65)
else:
    print("no se cumple")