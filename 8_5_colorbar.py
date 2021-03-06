#8.5. COLORBAR

import numpy as np
import matplotlib.pyplot as plt

# Set up some generic data
N = 37
x, y = np.mgrid[:N, :N]
Z = (np.cos(x*0.2) + np.sin(y*0.3))

# Mask out the negative and positive values, respectively
Zpos = np.ma.masked_less(Z, 0) 
Zneg = np.ma.masked_greater(Z, 0)

fig, (ax1, ax2, ax3) = plt.subplots(figsize=(13, 3), ncols=3)


# POSITIVE DATA (plot that is placed in left position)
# Plot just the positive data and save the color "mappable" object returned by ax1.imshow
pos = ax1.imshow(Zpos, cmap='Blues', interpolation='none')

# Add the colorbar using the figure's method, telling which mappable we're talking about and which axes object it should be near
fig.colorbar(pos, ax=ax1)


# NEGATIVE DATA (plot that is placed in central position)
# Plot just the negative data and save the color "mappable" object returned by ax2.imshow
neg = ax2.imshow(Zneg, cmap='Reds_r', interpolation='none')

# Add the colorbar using the figure's method, telling which mappable we're talking about and which axes object it should be near
fig.colorbar(neg, ax=ax2)


#PLOT BOTH POSITIVE AND NEGATIVE VALUES BETWEEN vmin AND vmax (plot that is placed in right position)
pos_neg_clipped = ax3.imshow(Z, cmap='RdBu', vmin=-1.2, vmax=1.2, interpolation='none')

#Add a colorbar to make it easy to read the values off the colorbar.
cbar = fig.colorbar(pos_neg_clipped, ax=ax3, extend='both')


plt.show()
