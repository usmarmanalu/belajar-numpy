import numpy as np

a = np.array([(1,-1), (1,1)])
print(a)

#inverse matriks
a_inverse = np.linalg.inv(a)
print(a_inverse)

#determinan matriks
a_determinan = np.linalg.det(a)
print(a_determinan)

#menghitung determinan inverse
a_determinan_inverse = np.linalg.det(a_inverse)
print(a_determinan_inverse)