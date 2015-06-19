from pylab import *

v0 = 0.0
m = 70.
#C = 1.4
#rho = 1.0
#A = 0.7
g = 9.81
#C_p = 1.8
#A_p = 44
k = 40
D = 10

def r(x):
	if x > 0:
		return 0
	else:
		return -k*x

def a(x, v):
    return r(x)/m - g - D/m*v

x0 = 20
dt = 1e-3
T = 60
N = int(ceil(T/dt))	# number of mesh cells

v = zeros(N+1)
x = zeros(N+1)
gkrefter = zeros(N+1)

v[0] = v0
x[0] = x0

t = linspace(0, T, N+1)

for i in range(N):
    gkrefter[i] = a(x[i], v[i])/g +1
    v[i+1] = v[i] + a(x[i], v[i])*dt
    x[i+1] = x[i] + v[i]*dt + 0.5*a(x[i], v[i])*dt**2

plot(t, x)
grid()
show()

