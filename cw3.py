import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
for i in range(10):
    grafic = '{}0 mm.txt'.format(i)
    file = open(grafic, 'r')
    try:
        data = file.readlines()
    finally:
        file.close()
    y = np.array(data[4:], dtype='i')
    x = np.arange(-50, 50)
    ax.plot(x, y)
plt.show()
