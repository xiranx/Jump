import numpy as np
a=np.array([182,216,200])
b=np.array([147,224,196])
c=np.linalg.norm(a-b)
d=0
for i in range(3):
    d=d+(a[i]-b[i])**2
f=d**0.5
print(c)
print(f)
