def f(x):
    return (x**2-1)/3

p_0=-0.0

for i in range(20):
    p_1=f(p_0)
    p_0=p_1
    print(f"imprimeme {p_0}")

