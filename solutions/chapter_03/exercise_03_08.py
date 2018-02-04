### (1)

from trapeze import trapeze



### (2)

from math import sin, pi
n = 1
s = 0
while 2 - s >= 1.E-6:   # sin is concave on [0,pi] -> estimate too small
    n += 1              # can skip n = 1 because it results in 0
    s = trapeze(sin, 0, pi, n)

print("Estimate for integral of sin from 0 to pi using trapeze:")
print(s)

### OUTPUT:
#   Estimate for integral of sin from 0 to pi using trapeze:
#   1.9999990007015205
