# Import everything we need
from pylab import *

# Define physical parameters used in simulation
m = 80
g = 9.81
Cd = 1.4
rho = 1
A = 0.7
k = 70

# Define time constants and number of steps
dt = 0.01
N = 60*100

# Define empty arrays
t = zeros(N+1)
a = zeros(N+1)
v = zeros(N+1)
x = zeros(N+1)

# Define inital conditions
v[0] = 0
x[0] = 20

# Define the force
def F(x, v, t):
	return -0.5*A*Cd*rho*abs(v)*v-m*g - k*x*(x < 0)

# Euler method loop
for i in range(N):
	t[i+1] = t[i] + dt
	a[i] = F(x[i], v[i], t[i])/m
	v[i+1] = v[i] + a[i]*dt
	x[i+1] = x[i] + v[i]*dt

# Plot results
gforces = a/g + 1
plot(t, x)
grid()
show()
	
