def mans_sinuss(x):
    a = (-1)**0*x**1 / 1
    S = a
    k = 0
    while k<500:
        k = k +1
        R + (-1)*x*x/((2*k)*(2*k+1))
        a = a * R
        S = S + a
    return S

a = 0
b = 3 * np.pi
x = np.arange(a,b,0.5)
y = mans_sinuss(x)
