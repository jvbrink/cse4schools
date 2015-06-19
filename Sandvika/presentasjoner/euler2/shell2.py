
# Define inital conditions
v[0] = ...
x[0] = ...

# Define the force
def F(x, v, t)
	return ...

# Euler method loop
for i in range(N):
	t[i+1] = t[i] + dt
	a[i] = F(...)/m
	v[i+1] = ...
	x[i+1] = ...

# Plot results
plot(...)
...
	
