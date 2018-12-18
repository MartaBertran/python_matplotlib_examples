# 2.15. IMAGE DEMO
# The most common way to plot images in Matplotlib is using imshow()
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

# Generation of a simple bivariate normal distribution
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x,y)
Z1 = np.exp(-X**2 -Y**2)
Z2 = np.exp(-(X-1)**2-(Y-1)**2)
Z = (Z1-Z2)*2

# Plot the image
fig, ax = plt.subplots()
im = ax.imshow(Z, interpolation='bilinear', cmap=cm.RdYlGn, origin='lower', extent=[-3, 3, -3, 3], vmax=abs(Z).max(), vmin=-abs(Z).max())
plt.title('Image Demo')
plt.show()
