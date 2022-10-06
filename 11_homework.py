import camelcase
c= camelcase.CamelCase()
txt= "Hello is a hey"
print(c.hump(txt))


import matplotlib

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = np.linspace(-10,10)
y = x**3

# plot
fig, ax = plt.subplots()



t = np.arange(-10,10,1)
plt.subplots_adjust(left=0.3,bottom=0.3, top = 0.9, right = 0.9)

# red dashes, blue squares and green triangles
plt.plot(t, t**3, 'b--')
plt.xlabel('x')
plt.ylabel('x^3')
ax.grid(True, which='both')


plt.show()