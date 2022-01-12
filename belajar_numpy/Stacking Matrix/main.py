import numpy as np

#array
a = np.array([1,2,3])
b = np.array([4,5,6])

#matrix
aMat = np.zeros((2,3))
bMat = np.ones((2,3))

#stacking array(menumpuk array)
print("stacking array : ")
c = np.hstack((a,b))  #secara horizontal
d = np.vstack((a,b))  #secara vertikal
print(c)
print(d)

#stacking matrix(menumpuk matrix)
print("stacking matrix : ")
cMat = np.hstack((aMat,bMat))       #secara horizontal
dMat = np.vstack((aMat,bMat))       #secara vertikal
print(cMat)
print(dMat)
