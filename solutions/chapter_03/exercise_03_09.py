# Exercise 3.9 (1)

def trapeze(f, a, b, mmax):
    integrals = []              # list of the approximations
    values = [f(a), f(b)]       # list of the calculated values
    for m in range(1,mmax+1):
        n = 2**m
        for k in range(1,n,2):
            values.insert(k, f(a + (k/n)*(b-a)))    # add new values
        integral = 0
        for i in range(len(values)-1):
            integral += values[i] + values[i+1]
        integral = (b-a)*integral/n/2
        integrals.append(integral)                  # add new approx.
    return integrals

### RESULTS
#
#   >>> from math import sin, pi
#   >>> m = 10
#   >>> results = trapeze(sin, 0, pi, m)
#   >>> for i in range(m):
#   ...     print("m={:2d}\t{}\t{:.20f}".format(i+1, results[i], 2-results[i]))
#   ... 
#   m= 1    1.5707963267948966      0.42920367320510344200
#   m= 2    1.8961188979370398      0.10388110206296019555
#   m= 3    1.9742316019455508      0.02576839805444919307
#   m= 4    1.9935703437723395      0.00642965622766045186
#   m= 5    1.9983933609701445      0.00160663902985547224
#   m= 6    1.9995983886400386      0.00040161135996141795
#   m= 7    1.9998996001842035      0.00010039981579645918
#   m= 8    1.9999749002350518      0.00002509976494824429
#   m= 9    1.9999937250705773      0.00000627492942273378
#   m=10    1.9999984312683816      0.00000156873161838433
#
###


### Exercise 3.9 (2)
#
#   Der Fehler viertelt sich jeweils.
#
#   >>> for i in range(m-2):
#   ...     print( (results[i] - results[i+1])/(results[i+1] - results[i+2]) )
#   ... 
#   4.164784400584785
#   4.039182316416593
#   4.009677144752887
#   4.002411992937073
#   4.00060254408483
#   4.000150607761501
#   4.000037649528035
#   4.000009414842847
#
###


### Exercise 3.9 (3)
#   
#   >>> m = 10
#   >>> f = (lambda x : 3**(3*x-1))
#   >>> results = trapeze( f, 0, 2, m)
#   >>> for i in range(m):
#   ...     print("m={:2d}\t{:24.20f}".format(i+1, results[i]))
#   ... 
#   m= 1    130.66666666666665719276
#   m= 2     89.58204463929762084717
#   m= 3     77.74742639121230070032
#   m= 4     74.66669853961546721166
#   m= 5     73.88840395800384897029
#   m= 6     73.69331521665949935596
#   m= 7     73.64451070980437918934
#   m= 8     73.63230756098684537392
#   m= 9     73.62925664736960129630
#   m=10     73.62849391106399821183
#   
#   >>> for i in range(m-2):
#   ...     (results[i] - results[i+1])/(results[i+1] - results[i+2])
#   ... 
#   3.471562932248868
#   3.841500716121706
#   3.958305665211694
#   3.9894387356667425
#   3.9973509398114637
#   3.9993371862347957
#   3.9998342622879792
#   3.999958563440565
#
###
