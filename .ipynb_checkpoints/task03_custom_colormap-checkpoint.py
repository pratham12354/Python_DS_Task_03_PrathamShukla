# Task 03: Implement a custom colormap for a Matplotlib plot
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Define colors for the custom colormap (from dark blue → white → dark red)
colors = ["#00008B", "#FFFFFF", "#8B0000"]
custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", colors, N=256)

# Generate sample data
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

# Apply custom colormap in plot
plt.figure(figsize=(6,5))
plt.contourf(X, Y, Z, 100, cmap=custom_cmap)
plt.colorbar(label="Intensity")
plt.title("Custom Colormap Example", fontsize=14)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
