### Exercise 3.9 (1)

from trapeze import powertrapeze

from math import sin, pi
m = 10
results = powertrapeze(sin, 0, pi, m)
print("Calculating trapeze estimate for integral of sin from 0 to pi with 2^m intervals:")
print(" m \testimate \t\terror")
for i in range(m):
    print("{:2d}\t{}\t{:.20f}".format(i+1, results[i], 2-results[i]))

#   Calculating trapeze estimate for integral of sin from 0 to pi with 2^m intervals:
#    m      estimate                error
#    1      1.5707963267948966      0.42920367320510344200
#    2      1.8961188979370398      0.10388110206296019555
#    3      1.9742316019455508      0.02576839805444919307
#    4      1.9935703437723395      0.00642965622766045186
#    5      1.9983933609701445      0.00160663902985547224
#    6      1.9995983886400386      0.00040161135996141795
#    7      1.9998996001842035      0.00010039981579645918
#    8      1.9999749002350518      0.00002509976494824429
#    9      1.9999937250705773      0.00000627492942273378
#   10      1.9999984312683816      0.00000156873161838433



### Exercise 3.9 (2)

#   Der Fehler viertelt sich jeweils.

print("Quotients any two subsequent differences of estimates:")
for i in range(m-2):
    q = (results[i] - results[i+1]) / (results[i+1] - results[i+2])
    print(q)

#   Quotients any two subsequent differences of estimates:
#   4.164784400584785
#   4.039182316416593
#   4.009677144752887
#   4.002411992937073
#   4.00060254408483
#   4.000150607761501
#   4.000037649528035
#   4.000009414842847



### Exercise 3.9 (3)

m = 10
f = (lambda x : 3**(3*x-1))
results = powertrapeze( f, 0, 2, m)
print("Calculating trapeze estimate for integral of 3^(3x-1) from 0 to 2 with 2^m intervals:")
print(" m \testimate")
for i in range(m):
    print("{:2d}\t{:24.20f}".format(i+1, results[i]))

#   Calculating trapeze estimate for integral of 3^(3x-1) from 0 to 2 with 2^m intervals:
#    m      estimate
#    1      130.66666666666665719276
#    2       89.58204463929762084717
#    3       77.74742639121230070032
#    4       74.66669853961546721166
#    5       73.88840395800384897029
#    6       73.69331521665949935596
#    7       73.64451070980437918934
#    8       73.63230756098684537392
#    9       73.62925664736960129630
#   10       73.62849391106399821183

print("Quotients any two subsequent differences of estimates:")
for i in range(m-2):
    q = (results[i] - results[i+1])/(results[i+1] - results[i+2])
    print(q)

#   Quotients any two subsequent differences of estimates:
#   3.471562932248868
#   3.841500716121706
#   3.958305665211694
#   3.9894387356667425
#   3.9973509398114637
#   3.9993371862347957
#   3.9998342622879792
#   3.999958563440565
