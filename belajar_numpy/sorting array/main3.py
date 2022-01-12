import numpy as np

dtipe = [("nama", "S102"), ("tinggi", int)]

data = [
    ("Usmar", 170),
    ("Andi", 180),
    ("Budi",160)
]

a = np.array(data, dtype= dtipe)
print(a)

print(np.sort(a, order="tinggi"))
print(np.sort(a, order="nama"))