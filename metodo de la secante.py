def f(x):
    return (((x**2)-1)/3)


pm_0=int(input("ingrese un numero: "))
pm_1=int(input("ingrese un numero: "))


for i in range(50):
        if f(pm_1)==f(pm_0):
            print(f"Ya estas {pm_2}")
            break
        
        pm_2=pm_1-((pm_1-pm_0)*(f(pm_1))/(f(pm_1)-f(pm_0)))
        pm_0=pm_1
        pm_1=pm_2
        print(f"imprimeme {pm_2}")
