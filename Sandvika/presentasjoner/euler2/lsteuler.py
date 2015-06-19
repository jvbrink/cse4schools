for i in range(N):
	a[i] = F(x[i], v[i], t[i])/m
	v[i+1] = v[i] + a[i]*dt
	x[i+1] = x[i] + v[i]*dt + 0.5*a[i]*dt**2
	