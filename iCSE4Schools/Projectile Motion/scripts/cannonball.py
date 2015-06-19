# Import various functions meant for numerical science
from pylab import *

def cannonball(F, theta):
	# Create empty 2D arrays
	N = len(t)-1
	r = zeros((N+1, 2))
	v = zeros((N+1, 2))
	a = zeros((N+1, 2))

	# Set initial conditions
	v[0] = (100*cos(theta), 100*sin(theta)) # inital velocity, m/s
	r[0] = (0,1)  # initial position, m

	# Solving equations of motion iteratively
	for i in range(N):
		a[i] = F(r[i], v[i], t[i])/m
		v[i+1] = v[i] + a[i]*dt
		r[i+1] = r[i] + v[i]*dt

	# Extract x and y coordinates as arrays
	x = r[:,0]
	y = r[:,1]

	# Return results
	return x, y


t_0 = 0 # Start time, s
t_end = 20 # End time, s
N = 10000 # Number of time steps

# Create a uniformly spaced time-array
t = linspace(t_0, t_end, N+1)

# Calculate the size of a time step
dt = t[1] - t[0]

m = 5.5 # mass, kg
g = 9.81 # acceleration of gravity, m/s^2
rho = 1.3 # air density, kg/m^3
C_D = 0.45 # drag coefficient
d = 0.11 # diameter of cannonball, m
A = pi*d**2 # cross-sectional area, m^2

def Fd(r, v, t):
	return array((0, -m*g))-0.5*rho*C_D*A*abs(v)*v
def Fg(r, v, t):
	return array((0, -m*g))

for theta in pi/3., pi/4., pi/6., pi/12.:
	x, y = cannonball(Fd, theta)
	plot(x,y)

# Prettify the plot
xlabel('Horizontal distance, [m]')
ylabel('Vertical distance, [m]')
title('Trajectory of a fired cannonball')
grid()
axis([0, 550, 0, 250])
legend(["60 deg", "45 Deg", "30 deg", "15 deg"])

# Makes the plot appear on the screen
savefig('plot_cannonball3.pdf')
show()

