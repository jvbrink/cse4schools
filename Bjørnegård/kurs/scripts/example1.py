from pylab import *

m = 0.056
D = 0.001
g = 9.81

def F(x, v, t):
	return -m*g-D*v*abs(v)

N = 10000
t0 = 0
tend = 10
x0 = 1
v0 = 10

a = zeros(N+1)
v = zeros(N+1)
x = zeros(N+1)
t = linspace(t0,tend,N+1)
dt = t[1]-t[0]

x[0] = x0
v[0] = v0

for i in range(N):
	if x[i] < 0:
		a[i] = -2*v[i]/dt
		v[i+1] = -0.9*v[i]
		x[i+1] = -x[i]
	else:	
		a[i] = F(x[i], v[i], t[i])/m
		v[i+1] = v[i] + a[i]*dt
		x[i+1] = x[i] + v[i]*dt

plot(t, x)
show()