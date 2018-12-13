# 8.2. COLOR BY Y-VALUE

import numpy as np
import matplotlib.pyplot as plt

# Numpy arrange returns evenly spaced values within a given interval
t = np.arange(0.0, 2.0, 0.01)
#Numpy trigonometric sine
s = np.sin(2*np.pi*t)

# Upper and lower limits are defined to change the colors
upper = 0.77
lower = -0.77

# Numpy masked array is used
supper = np.ma.masked_where(s < upper, s)
slower = np.ma.masked_where(s > lower, s)
smiddle = np.ma.masked_where(np.logical_or(s < lower,s > upper), s)

# Plot the figure
fig, ax = plt.subplots()
ax.plot(t, smiddle, t, slower, t, supper)
plt.show()
