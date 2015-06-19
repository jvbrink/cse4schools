from pylab import *

m = 90
g = 9.81
rho = 1
A = 0.7
C = 1.4
A_p = 44
C_p = 1.8
v0 = 0

def a(v):
    return g - 0.5*rho*C*A/m*v*v

dt = 0.01
T = 180
n = int(T/dt)

t = zeros(n+1)
v = zeros(n+1)
gforces = zeros(n+1)

# Simuler de forste 60 sekundene
for i in range(0, int(60/dt)):
    t[i+1] = t[i] + dt
    v[i+1] = v[i] + a(v[i])*dt
    gforces[i] = 1 - a(v[i])/g

# Simulerer de neste 5 sekundene
for i in range(int(60/dt), int(65/dt)):
    C += (C_p-C)/(5/dt)
    A += (A_p-A)/(5/dt)

    t[i+1] = t[i] + dt
    v[i+1] = v[i] + a(v[i])*dt
    gforces[i] = 1 - a(v[i])/g

# Simuler de siste 115 sekundene
for i in range(int(65/dt), int(180/dt)):
    t[i+1] = t[i] + dt
    v[i+1] = v[i] + a(v[i])*dt
    gforces[i] = 1 - a(v[i])/g



plot(t,gforces)
xlabel('t')
ylabel('v(t)')
grid()
show()