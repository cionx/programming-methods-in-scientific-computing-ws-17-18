print("Calculate machine epsilon:")
eps = 1.0
i = 0
while 1+eps > 1:
  eps = eps/2
  i += 1
eps *= 2
print("eps: {}".format(eps))
print("iterations: {}".format(i))

print("With different loop condition:")
eps = 1.0
i = 0
while eps > 0:
  eps /= 2
  i += 1
eps *= 2
print("eps: {}".format(eps))
print("iterations: {}".format(i))
