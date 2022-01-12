import numpy as np

#list python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

#array numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

#penjumlahan
hasil1 = a+b
#elementwise operation(menambahkan tiap kolom array)
hasil2 = anp+bnp

#pengurangan
hasil3 = anp-bnp

#perkalian
hasil4 = anp*bnp

#pembagian
hasil5 = anp/bnp

#kuadrat
hasil6 = anp**2

#multidimensi array numpy
c = np.array(([1,2,3], [4,5,6]))
d = np.array(([7,8,9], [-1,-2,-3]))
hasil7 = c + d
hasil7 = c * d


print(hasil1)
print(hasil2)
print(hasil3)
print(hasil4)
print(hasil5)
print(hasil6)
print(hasil7)
