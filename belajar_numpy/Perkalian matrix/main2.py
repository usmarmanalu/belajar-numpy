import numpy as np

a = np.array(([1,2,5],
              [3,4,6]))

b = np.ones([3,1])

print("matriks a :")
print(a)

print("matriks b :")
print(b)

#perkalian matriks

c1 = np.dot(a,b)
c2 = a.dot(b)

print("matriks c1 :")
print(c1)

print("matriks c2 :")
print(c2)