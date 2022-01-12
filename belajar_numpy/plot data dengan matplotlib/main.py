import numpy as np
import matplotlib.pyplot as plt


# persamaan garis
# y = 2x + 3

x = np.arange(0,11,1)
y = 2 * x + 3
print(x)
print(y)

plt.plot(x,y)
plt.ylabel("Label Y")
plt.xlabel("Label X")
plt.show()