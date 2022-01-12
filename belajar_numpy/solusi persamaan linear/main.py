import numpy as  np

a = np.array([(2,3), (1,2)])
y = np.array([23,14])
print(a)
print(y)

a_inverse = np.linalg.inv(a)

#menyelesaikan persamaan linear
x1 = np.dot(a_inverse, y)
print(x1)

#cara lain
x2 = np.linalg.solve(a,y)
print(x2)