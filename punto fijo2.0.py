def f(x):
    return x-((x**3+4*x**2-10)/(3*x**2+8*x))
#(10/(4+x))**(1/2)#en todos si da
#(1/2)*(10-x**3)**(1/2)#p_0=2
#(10/x - 4*x)**(1/2)
#x+x**3 + 4*x**2-10

p_0=2


for i in range(20):
    p_1=f(p_0)
    p_0=p_1
    print(f"imprimeme {p_0}")