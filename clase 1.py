import math
valor_verdadero=math.exp(0.5)
tolerancia=0.005

serie=1
n=1
error=100

while(error<tolerancia):
    valor_anterior=serie
    serie=serie+((0.5)**n)/(math.factorial(n))
    valor_actual=serie
    
    error_verdadero=abs((valor_verdadero - serie)/valor_verdadero)
    error_porcental=abs((valor_actual- valor_anterior)/valor_actual)
    error=max(error_verdadero, error_porcental)
    
    print("terminos \t resultado \t errort \t errorRe")
    print(f"{n} \t {serie} \t {error_verdadero} \t {error_porcental}")
    n=n+1
 
 