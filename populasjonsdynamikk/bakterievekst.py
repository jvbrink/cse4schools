
from pylab import *



n = 24*2    #antall tidsintervaller
y0 = 1    #antall harer nar vi starter
r1 = 1   #vekstrate (dvs 100% per time)
r2 = 0
r3 = -0.3
index_set = range(n+1)
y = zeros(len(index_set))
y[0] = y0
for k in index_set[:-1]:
    if k < 15: 
        y[k+1] = y[k] + r1*y[k]
    elif k < 18:
        y[k+1] = y[k] + r2*y[k]
    else:
        y[k+1] = y[k] + r3*y[k]

plot(index_set, y)
show()
