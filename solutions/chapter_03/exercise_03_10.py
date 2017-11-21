from trapeze import powertrapeze

# It sufficies to use se m = 11, see text for more details

from math import exp
f = (lambda x: exp(x**2))
m = 11
results = powertrapeze(f, 0, 1, m)
print("Calculating trapeze estimate for integral of e^(x^2) from 0 to 1 with 2^m intervals:")
for i in range(m):
    print("m={:2d}\t{:24.20f}".format(i+1, results[i]))

#   Calculating trapeze estimate for integral of e^(x^2) from 0 to 1 with 2^m intervals:
#   m= 1      1.57158316545863208091
#   m= 2      1.49067886169885532865
#   m= 3      1.46971227642966528748
#   m= 4      1.46442031014948170764
#   m= 5      1.46309410260642858148
#   m= 6      1.46276234857772702291
#   m= 7      1.46267939741858832292
#   m= 8      1.46265865883777390621
#   m= 9      1.46265347414312651964
#   m=10      1.46265217796637525538
#   m=11      1.46265185392199392744
