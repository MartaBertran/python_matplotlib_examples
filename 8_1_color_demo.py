#8.1. COLOR DEMO

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0.0, 2.0, 201)
s = np.sin(2*np.pi*t)

# 1) RGB tuple:
# For the background of the figure
fig, ax = plt.subplots(facecolor=( .18, .30, .50))

# 2) Hex string:
# Used in the square surroundex by the axes
ax.set_facecolor('#eafff5')

# 3) Gray level string:
# Used for the title
ax.set_title('Voltage vs. time chart', color='0.9')

# 4) Single letter color string:
# Used for the x axis label
ax.set_xlabel('time (s)', color='c')

# 5) A named color:
# Used for the y axis label
ax.set_ylabel('voltage (mV)', color='peachpuff')

# 6) A named xkcd color:
# In the continuous line of the plot
ax.plot(t, s, 'xkcd:crimson')

# 7) Cn notation:
# In the discontinuous(--) line of the plot
ax.plot(t, .7*s, color='C4', linestyle='--')

# 8) Tab notation:
# For the color of the numbers in both x and y axis
ax.tick_params(labelcolor='tab:pink')


plt.show()
