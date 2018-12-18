# 3.16. GEOGRAPHIC PROJECTIONS
# Alternatives for geographic projections in Matlplotlib are: 'Basemaps Toolkit' and 'Cartopy'
import matplotlib.pyplot as plt

# Example 1 - Aitoff Projection
plt.figure()
plt.subplot(111, projection="aitoff")
plt.title("Aitoff")
plt.grid(True)

# Example 2 - Hammer Projection
plt.figure()
plt.subplot(111, projection="hammer")
plt.title("Hammer")
plt.grid(True)

# Example 3 - Lambert Projection
plt.figure()
plt.subplot(111, projection="lambert")
plt.title("Lambert")
plt.grid(True)

# Example 4 - Mollweide Projection
plt.figure()
plt.subplot(111, projection="mollweide")
plt.title("Mollweide")
plt.grid(True)
