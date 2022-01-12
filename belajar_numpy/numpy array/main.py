import numpy as np

print("membuat vector")
a = np.array([1,2,3,4,5])
b = np.array([1.5,2.5,3.5,4,5])

print(a)
print(b)

print("membuat vector dengan range")
c= np.arange(1,10,2)
print(c)

print("membuat linspace")
d = np.linspace(1,10,4)
print(d)

print("array multi dimensi/matriks")
e = np.array([(1,2,3), (4,5,6)])
print(e)
print(e+1)

print("matriks dengan nilao 0")
f = np.zeros((5,5))
print(f)

print("matriks dengan nilai 1")
g = np.ones((5,5))
print(g)

print("matriks identitas")
h1 = np.identity(5)
h2 = np.eye(5)
print(h1)
print(h2)
