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