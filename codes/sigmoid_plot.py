import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-4,4,1000)

def sigmoid(x):
    return 1/(1 + np.exp(-x))

plt.plot(X,sigmoid(X))
plt.grid()

plt.xlabel('$x$')
plt.ylabel('$sigmoid(x)$')

#plt.show()

plt.savefig('../figs/sigmoid_plot.png')