from pylab import *

def angular_acc(theta,omega,t):
	return 

N = 1000
t = linspace(0,10,N+1)
dt = t[1]-t[0]

theta = zeros(N+1)
omega = zeros(N+1)

R = 1
m = 2 
g = 9.81

theta[0] = pi/4.

for i in range(N):
	angular_acc = -m*g*sin(theta[i])/R
	omega[i+1] = omega[i] + angular_acc*dt
	theta[i+1] = theta[i] + omega[i+1]*dt

plot(t, theta)
xlabel("Time, [s]")
ylabel("Angle, [rad]")
title("Swinging Pendulum")
savefig("pendulumplot.pdf")
show()