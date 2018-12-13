import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

# Plot of main figure with normal x and y labels (XLabel0 and YLabel0)
fig = plt.figure(tight_layout=True)
gs = gridspec.GridSpec(2, 2)

# Main figure is created with subplots so that modified 
ax = fig.add_subplot(gs[0, :])
ax.plot(np.arange(0, 1e6, 1000))
ax.set_xlabel('XLabel0')
ax.set_ylabel('Ylabel0')

# For the 2 subplots the axes are defined as follows
for i in range(2):
    ax = fig.add_subplot(gs[1, i])
    ax.plot(np.arange(1., 0., -0.1) * 2000., np.arange(1., 0., -0.1))
    ax.set_ylabel('YLabel1 %d' % i)
    ax.set_xlabel('XLabel1 %d' % i)
    if i == 0:
        for tick in ax.get_xticklabels():
            tick.set_rotation(55)
            
# Align x and y labels, it is the same as fig.align_xlabels(); fig.align_ylabels()
fig.align_labels()  

# Plot the figures
plt.show()
