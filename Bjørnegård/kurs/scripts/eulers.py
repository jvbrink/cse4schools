from pylab import *

N = 25
Ne = 1000

t = linspace(0,5,N+1)
te = linspace(0,5,Ne+1)

dt = t[1]-t[0]
dte = te[1]-te[0]

v = zeros(N+1)
ve = zeros(Ne+1)

v[0] = 1
ve[0] = 1

for i in range(N):
	v[i+1] = v[i] + (10 - v[i])*dt
for i in range(Ne):
	ve[i+1] = ve[i] + (10 - ve[i])*dte

plot(t, v, 'o--')
plot(te, ve)
axis([0,5,0,12])
show()
