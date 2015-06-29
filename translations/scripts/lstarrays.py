# Import various functions meant for numerical science
import numpy as np 

t_0 = 0 # Start time, s
t_end = 10 # End time, s
N = 1000 # Number of time steps

# Create a uniformly spaced time-array
t = np.linspace(t_0, t_end, N+1)

# Calculate the size of a time step
dt = t[1] - t[0]

# Create empty acceleration, velocity and position arrays
a = np.zeros((2, N+1))
v = np.zeros((2, N+1))
r = np.zeros((2, N+1))

# Set initial conditions
v[0] = (100*cos(pi/6), 100*sin(pi/6)) # inital velocity, m/s
r[0] = (0,1)  # initial position, m
