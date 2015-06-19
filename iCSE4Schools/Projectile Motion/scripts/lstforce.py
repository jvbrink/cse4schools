m = 5.5 # mass, kg
g = 9.81 # acceleration of gravity, m/s^2
rho = 1.3 # air density, kg/m^3
C_D = 0.45 # drag coefficient
d = 0.11 # diameter of cannonball, m
A = pi*d**2 # cross-sectional area, m^2

def F(r, v, t):
	return (0, -m*g) - 0.5*rho*C_D*A*abs(v)*v