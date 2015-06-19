# Import everything we need
from pylab import *

# Define physical parameters used in simulation
m = 90
g = 9.81
Cd = 1.4
rho = 1
A = 0.7
A_p = 44
Cd_p = 1.8

# Define time constants and number of steps
dt = 0.01
N = 40*100

# Define empty arrays
t = zeros(N+1)
a = zeros(N+1)
v = zeros(N+1)
x = zeros(N+1)

# Define inital conditions
v[0] = 0
x[0] = 4000

# Define the force
def F(x, v, t):
	return -0.5*A*Cd*rho*abs(v)*v-m*g

# Euler method loop
for i in range(N):
	t[i+1] = t[i] + dt
	a[i] = F(x[i], v[i], t[i])/m
	v[i+1] = v[i] + a[i]*dt
	x[i+1] = x[i] + v[i]*dt

	if 60. < t[i] < 65.:
		Cd += (Cd_p - Cd)/(5/dt)
		A  += (A_p  - A)/(5/dt)

# Plot results
gforces = a/g + 1
plot(t, gforces)
grid()
show()
	
