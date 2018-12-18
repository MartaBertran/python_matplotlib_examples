# 5.1. BASIC PIE CHART
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise
labels = 'Apples', 'Oranges', 'Bananas', 'Pears'
# Amount of each type of fruit in %
sizes =  [15, 30, 45, 10]
# Only the 2nd slice is "exploded" (i.e. 'Oranges')
explode = (0, 0.1, 0, 0)

# Plot the pie chart
fig1, ax1 = plt.subplots()
# The default startangle is 0, which would start the 'apples' slice on the positive x-axis. 
# But, in this example, the startangle = 90 so that everything is rotated counter-clockwise by 90 degrees and the 'apples' slice starts on the positive y-axis.
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
# In order to ensure that the pie is drawn as a circle, equal aspect ratio is set
ax1.axis('equal')

plt.show()
