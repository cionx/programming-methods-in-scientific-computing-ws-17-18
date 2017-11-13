from math import sin, pi

# Exercise 3.8 (1)

def trapeze(f,a,b,n):
    values = [f(a + (k/n)*(b-a)) for k in range(n+1)]
    integral = 0
    for i in range(len(values)-1):
        integral += values[i] + values[i+1]
    integral = (b-a)*integral/n/2
    return integral

# Exercise 3.8 (2)

n = 1
s = 0
while 2 - s >= 1.E-6:           # sin is concave on the interval -> estimate always to small
    n += 1                      # can skip n = 1 because it results in 0
    s = trapeze(sin, 0, pi, n)

print(s)
