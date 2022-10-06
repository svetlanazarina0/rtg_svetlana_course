import matplotlib.pyplot as plt
import numpy as np
print(plt.style.available)


font = {'family' : 'normal',
        'size'   : 8}


plt.style.use('dark_background')


x = np.linspace(-10,10)
y = x**3
fig, ax = plt.subplots()
t = np.arange(-10,10,1)
plt.subplots_adjust(left=0.3,bottom=0.3, top = 0.9, right = 0.9)

# red dashes, blue squares and green triangles
plt.plot(t, t**3, 'b--', linewidth=3)
plt.xlabel('x' ,**font)
plt.ylabel('x^3',**font)
ax.grid(True, which='both')
plt.yticks(fontsize=8)
plt.xticks(fontsize=8)

plt.show()

