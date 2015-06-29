for i in range(N):
	a[i] = F(r[i], v[i], t[i])/m
	v[i+1] = v[i] + a[i]*dt
	r[i+1] = r[i] + v[i]*dt
	