# Extract x and y coordinates
x = r[:,0]
y = r[:,1]

# Import functionality for plotting
from matplotlib.pyplot import plt

# Plot figure
plt.plot(x,y)

# Prettify the plot
plt.xlabel('Horizontal distance, [m]')
plt.ylabel('Vertical distance, [m]')
plt.title('Trajectory of a fired cannonball')
plt.grid()
plt.axis([0, 900, 0, 250])

# Makes the plot appear on the screen
plt.show()