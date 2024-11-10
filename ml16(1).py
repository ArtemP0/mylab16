import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.2, 10.2)
y = np.log(x) * np.cos(x) + np.log10(x) * np.cos(x)

plt.plot(x, y, color='yellow', linestyle='-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції')
plt.savefig("triangle.svg", format="svg")
plt.show()
