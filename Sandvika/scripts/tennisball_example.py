from pylab import *

# Define time constant and number of steps
dt = ...
N = ...

# Create empty arrays
t = zeros(N+1)
a = zeros(N+1)
v = zeros(N+1)
x = zeros(N+1)

# Define initial conditions
v[0] = ...
x[0] = ...

# Define force as a function
def F(x, v, t):
	return ...

# Euler method loop (calculate x and v)
for i in range(N):
	a[i]   = F(...)/m
	t[i+1] = ...
	v[i+1] = ...
	x[i+1] = ...

# Plot results
plot(t, x)
xlabel('t')
ylabel('v')
grid()
axis([0, 3, 0, 6.5])
show()
