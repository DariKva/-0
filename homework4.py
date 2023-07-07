import matplotlib.pyplot as plt
import numpy as np
import random

n = int(input())
x = np.array([])
for i in range(n):
    i = random.randint(0, 100)
    x = np.append(x, i)
y = np.array([], dtype="f")
pogre = 0
ky = random.uniform(0, 3)
by = random.uniform(0, 7)
for k in range(n):
    pogre = random.randint(-10, 10)
    y = np.append(y, ((float(x[k] * ky)) + by + pogre))


def sred(mass, n):
    sum = 0
    count = np.size(mass)
    for num in mass:
        sum += num ** n
    return sum / count


def kb(x, y):
    soed = np.array([], dtype='f')
    for l in range(np.size(x)):
        soed = np.append(soed, x[l] * y[l])
    k = (sred(soed, 1) - sred(x, 1) * sred(y, 1)) / (sred(x, 2) - sred(x, 1) ** 2)
    b = sred(y, 1) - k * sred(x, 1)
    dk = (1 / (n ** 0.5)) * (((sred(y, 2) - sred(y, 1) ** 2) / (sred(x, 2) - sred(x, 1) ** 2) - k ** 2) ** 0.5)
    db = dk * ((sred(x, 2) - sred(x, 1) ** 2) ** 0.5)
    otvet = [k, b, dk, db]
    return otvet


y1 = np.array([])
idk = kb(x, y)
for h in range(n):
    h = x[h] * idk[0] + idk[1]
    y1 = np.append(y1, h)
fig, ax = plt.subplots()
x2 = [0, 100]
y2 = [by, ky * x2[1] + by]
ax.plot(x, y1)
ax.plot(x2, y2)
ax.scatter(x, y, s=2)
ax.set_title('Какие-то линии и точки')
plt.show()