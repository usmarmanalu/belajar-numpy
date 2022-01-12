import numpy as np


#membuat matrix dengan tipe data tertentu
a = np.array(([1,2,3],[3,4,5]),dtype = float)

#membuat array dengan menggunakan function
def kuadrat(baris, kolom):
    return kolom**2, baris**2

def jumlah(baris,kolom):
    return (kolom + baris)

b = np.fromfunction(kuadrat,(1,10), dtype=int)
c = np.fromfunction(jumlah,(4,4), dtype=float)

#membuat array atau matrix dengan menggunakan iterable
iterable = (x*2 for x in range(5))

d = np.fromiter(iterable, dtype=int)


#multitype array
dtpe = [('nama', "S5210"), ('tinggi', int)]

data = [
    ('asep', 150),
    ('andi', 160),
    ('arya', 180)
]

e = np.array(data, dtype=dtpe)
print(e)
