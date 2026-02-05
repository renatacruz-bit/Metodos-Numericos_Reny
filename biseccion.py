import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def biseccion(f, a, b, n_iter):

    if f(a)*f(b)>0:
        raise ValueError("f(a) y f(b) debe tener signo diferente")
    
    #punto medio inicial y lista de puntos medios
    p_anterior=(a+b)/2
    puntos_medios=[]

    #nombre de los valores de la tabla
    print(" n       a        b      p       f(p)       error relativo")
    print("-"*65)

    #ciclo principal de la biseccion
    for n in range(1, n_iter+1):
        #calcula el punto medio del intervalo actual
        p=(a+b)/2
        
        #ver si f(p)=0
        if f(p)==0:
            print(f"{n:2d} | {a:8.6f} {b:8.6f} {p:8.6f}"
                  f"{f(p):11.2e} {'0.00e+00':>13}" )

            print("la raiz exacta fue encontrada")
            break
        #calcular el error relativo
        error_rel=abs((p-p_anterior)/p)
        #guardar los puntos medios
        puntos_medios.append(p)
        
        #imprime la primera fila 
        print(f"{n:2d} | {a:8.6f} {b:8.6f} {p:8.6f}"
                    f"{f(p):11.2e} {error_rel:13.2e}" )
        
        #en que intervalo esta la raiz
        if f(a)*f(b)>0:
            a=p
        else:
            b=p

        p_anterior=p

    #regresa la ultima aproximacion y todos los puntos medias
    return p, puntos_medios

"ejemplos"
#definimos la funcion
def f(x):
    return x**3-x-2
#definimos los terminos e iteraciones
a=1
b=2
n_iter=20

#tolerancia
epsilon=1e-6

#invocamos el metodo de biseccion
raiz, puntos=biseccion(f, a, b, n_iter)

#muestra la aproximacion final
print(f"Aproximacion a la riz despues de {n_iter} iteraciones: {raiz}")

# ---------------------------------------------------------
# GRÁFICA Y ANIMACIÓN DE LA CONVERGENCIA
# ---------------------------------------------------------

# Genera puntos para dibujar la función
x = [a + i * (b - a) / 400 for i in range(401)]
y = [f(xi) for xi in x]

# Crea la figura y los ejes
fig, ax = plt.subplots()

# Dibuja la función f(x)
ax.plot(x, y, label="f(x)")

# Dibuja el eje x
ax.axhline(0, color="black")

# Configura los límites del gráfico
ax.set_xlim(a, b)
ax.set_ylim(min(y), max(y))

# Etiquetas y título
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Convergencia del método de Bisección")

# Objeto gráfico para los puntos medios (inicialmente vacío)
puntos_plot, = ax.plot([], [], 'ro', label="Puntos medios")

# Marca la raíz final
ax.plot(raiz, 0, 'ko', label="Raíz aproximada")

# Muestra la leyenda
ax.legend()

# ---------------------------------------------------------
# Función que actualiza la animación
# ---------------------------------------------------------
def actualizar(frame):
    
    x_data = puntos[:frame + 1]           # Puntos medios hasta el frame actual
    y_data = [0] * (frame + 1)             # Todos sobre el eje x
    puntos_plot.set_data(x_data, y_data)
    return puntos_plot,

# Crea la animación
anim = FuncAnimation(
    fig,
    actualizar,
    frames=len(puntos),
    interval=100,      # Tiempo entre frames (ms)
    repeat=False
)

# Muestra la animación
plt.show()