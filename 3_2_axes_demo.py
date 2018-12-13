# 3.2. AXES DEMO

# Creation of inset axes within the main plot axes

import matplotlib.pyplot as plt
import numpy as np

# Random state for reproducibility is fixed
np.random.seed(19680801)

# Some data is created to use for the plot
dt = 0.001
t = np.arange(0.0, 10.0, dt)
# Impulse response
r = np.exp(-t[:1000]/0.05)
x = np.random.randn(len(t))
# Colored noise
s = np.convolve(x, r)[:len(x)]*dt

# By default, the main axes is subplot(111)
plt.plot(t, s)
plt.axis([0, 1, 1.1 * np.min(s), 2 * np.max(s)])
plt.xlabel('time(s)')
plt.ylabel('current(nA)')
plt.title('Gaussian colored noise')

# Inset axes over the main axes
# axes limits are [xmin, ymin, xmax, ymax]
a = plt.axes([.65, .6, .2, .2], facecolor='k')
# histogram
n, bins, patches = plt.hist(s, 400, density=True)
plt.title('Probability')
plt.xticks([])
plt.yticks([])

# Another inset axes over the main axes
a = plt.axes([0.2, 0.6, .2, .2], facecolor='k')
plt.plot(t[:len(r)], r)
plt.title('Impulse response')
#xlim sets the x-axis view limits
plt.xlim(0, 0.2)
plt.xticks([])
plt.yticks([])

# Plot
plt.show()
