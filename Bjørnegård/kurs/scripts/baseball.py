from pylab import *

def baseball(F, r_0, v_0):
	# Create empty 2D arrays
	N = len(t)-1
	r = zeros((N+1, 2))
	v = zeros((N+1, 2))
	a = zeros((N+1, 2))

	# Set initial conditions
	v[0] = v_0
	r[0] = r_0

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

# Constants
g = 9.81 # gravitational acceleration, m/s^2
m = 0.145 # mass of ball, kg
A = pi*0.038**2 # cross-sectional area of ball, m^2
C_d = 0.3 # Drag coefficient of ball
rho = 1.2 # Density of air # kg/m^3

# Define the force functions
def F_with_drag(x,v,t):
    return -0.5*C_d*A*rho*abs(v)*v + (0, -m*g)
    
def F_without_drag(x,v,t):
    return array((0, -m*g))
    
# Simulation parameters
N = 1000 # Number of time steps
t_0 = 0 # Start time
t_end = 10 # End time, s
t = linspace(0, 10, N+1) # time-array
dt = t[1] - t[0] # size of time step

# Define initial conditions
r0 = (0, 1)


# Loop over various angles, calculating trajectories and plotting them
for angle in linspace(pi/6., pi/3., 1001):
	v0 = (40*cos(angle), 40*sin(angle))
	x, y = baseball(F_with_drag, r0, v0)
	print angle, max(x[y>0])

# Add other details to plot
axis([0, 150, 0, 50])
xlabel('Horizontal distance [m]')
ylabel('Vertical distance [m]')
legend(['15', '30', '45', '60'])
grid()
title('Path of a batted baseball at various angles')
savefig("baseball3.png")
show()