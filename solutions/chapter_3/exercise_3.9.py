from math import sin, pi

# Exercise 3.9 (1)

def trapeze(f, a, b, mmax):
    integrals = []
    values = [f(a), f(b)]
    for m in range(1,mmax+1):
        n = 2**m
        for k in range(1,n,2):
            values.insert(k, f(a + (k/n)*(b-a)))
        integral = 0
        for i in range(len(values)-1):
            integral += values[i] + values[i+1]
        integral = (b-a)*integral/n/2
        integrals.append(integral)
    return integrals

m = 18
results = trapeze(sin, 0, pi, m)
for i in range(m):
    print("m={:2d}\t{}\t{:.20f}".format(i+1, results[i], 2-results[i]))

# Exercise 3.9 (2)

Der Fehler viertelt sich jeweils.

for i in range(m-2):
    (results[i] - results[i+1])/(results[i+1] - results[i+2])


# Exercise 3.9 (3)

m = 18
results = trapeze( (lambda x : 3**(3*x-1)) , 0, 2, m)
for i in range(m):
    print("m={:2d}\t{:24.20f}".format(i+1, results[i]))

for i in range(m-2):
    (results[i] - results[i+1])/(results[i+1] - results[i+2])
