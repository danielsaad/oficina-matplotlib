import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
x = np.random.randn(1000)
y = np.random.randn(1000)
ax.scatter(x,y)
plt.show()
