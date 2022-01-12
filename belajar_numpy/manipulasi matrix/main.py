import numpy as np

a = np.array(([1,2,3],
              [4,5,6]))
print("matriks a dengan ukuran : ",a.shape)
print(a)

#transpose matrik(baris dijadikan kolom)
print("matriks a dengan ukuran : ",a.shape)
print("transpose matriks dari a :")
print(a.transpose())
#print(np.transpose(a))
#print(a.T)


#flatten array(membuat vector baris)
print("matriks a dengan ukuran : ",a.shape)
print("flatter matriks a :")
print(a.ravel())
#print(np.ravel(a))


#reshape matrix
print("matriks a dengan ukuran : ",a.shape)
print("reshape matriks a : ")
print(a.reshape(3,2))


#resize matriks
print("resize matriks a : ")
a.resize(3,2)
print(a)
print("matriks a dengan ukuran : ",a.shape)
