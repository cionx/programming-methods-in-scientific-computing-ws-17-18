print("Calculate machine epsilon:")
eps = 1.0
i = 0
while 1+eps > 1:
  eps /= 2
  i += 1
eps *= 2
print("eps: {}".format(eps))
print("iterations: {}".format(i))


#   OUTPUT:
#   Calculate machine epsilon:
#   eps: 2.220446049250313e-16
#   iterations: 53

print("With different loop condition:")
eps = 1.0
i = 0
while eps > 0:
  eps /= 2
  i += 1
eps *= 2
print("eps: {}".format(eps))
print("iterations: {}".format(i))


#   OUTPUT:
#   With different loop condition:
#   eps: 0.0
#   iterations: 1075

#   An explanation of this results can be found in the notes.

