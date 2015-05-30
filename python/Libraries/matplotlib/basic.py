from matplotlib import pyplot as plt
import numpy as np

energy = [-800, -802, -804, -803, -802]
bond = np.arange(1.0, 1.5, 0.1)

plt.plot(bond, energy)

plt.show()
