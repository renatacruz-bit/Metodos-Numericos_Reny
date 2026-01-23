import numpy as np


def f(x):
    return 1 / (1 + x**2)

# Valor a estimar
x_eval = -0.25
valor_real = f(x_eval)

# Polinomio de Taylor de orden 4 para f(x) = 1/(1+x^2) en x0=0
# Serie: 1 - x^2 + x^4 - x^6 + ...
# Orden 4 => P4(x) = 1 - x^2 + x^4
def taylor_p4(x):
    
    termino_orden_0 = 1.0          
    termino_orden_2 = -x**2       
    termino_orden_4 = x**4        
    polinomio = termino_orden_0 + termino_orden_2 + termino_orden_4
    
    return polinomio
    

# Calcular aproximacion
aproximacion = taylor_p4(x_eval)
error = abs(aproximacion - valor_real)

num_iteraciones = 4  

# Mostrar tabla
print("="*68)
print("Método           | Aproximación | Error absoluto | Orden del polinomio")
print("=" * 68)
print(f"Taylor (orden 4) | {aproximacion:12.8f} | {error:.2e}      | {num_iteraciones}")

# Graficar

x= np.linspace(-1, 1, 400)
y_real = f(x)
y_taylor = taylor_p4(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y_real, label='f(x) = 1/(1 + x**2)', color='blue')
plt.plot(x, y_taylor, '--', label='P4(x) = 1 - x**2 + x**2', color='green')

# Marcar el punto x = -0.25
plt.plot(x_eval, valor_real, 'bo', label=f'f({x_eval}) = {valor_real:.6f}')
plt.plot(x_eval, aproximacion, 'ro', label=f'P4({x_eval}) = {aproximacion:.6f}')

plt.title('Aproximación de f(x) con Polinomio de Taylor de Orden 4')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='red', linewidth=2)
plt.axvline(0, color='yellow', linewidth=1)
plt.show()