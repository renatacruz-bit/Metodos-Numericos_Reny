
def f(x):
    return (((x**2)-1)/3)
#((x**2)-2)
#(((x**2)-1)/3)
def df(x):
    return (2/3)*x
#(2*x)
#(2/3)*x

p_0=0.5

for i in range(50):
    p_1=p_0 -(f(p_0)/df(p_0))
    p_0=p_1
    print(f"imprimeme {p_0}")
