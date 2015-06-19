# Import necessary functionality
from pylab import *

# Define constants and parameters
v0 = 0.0
m = 90.
C = 1.4
rho = 1.0
A = 0.7
g = 9.81
C_p = 1.8
A_p = 44


D = C*rho*A/2.
D_p = C_p*rho*A_p/2.

# Set up time-array
dt = 1e-3
T  = 120.0
N = int(ceil(T/dt))	# number of mesh points
t = linspace(0, T, N+1)

t_p = 60.

# Set up velocity-array
v = zeros(N+1)

# Iterate through time (solve)
for i in range(N):
	if i*dt < t_p:
		a = g - D*abs(v[i])*v[i]/m
	else:
		a = g - D_p*abs(v[i])*v[i]/m
	v[i+1] = v[i] + a*dt

plot(t,v)
grid()
show()

# Print terminal velocity
print max(v)
print sqrt(m*g/D)

'''
class Solver:
	"""Class for solving the ODE"""

		

	def solve(self):
		"""Method for solving the problem from t=0 to t=T"""
		self.N = int(ceil(self.T/self.dt)) + 1	# number of mesh points
		self.v = zeros(self.N) 	    			# velocity array
		self.v[0] = self.problem.v0 	    	# initial velocity (m/s)
		self.t = linspace(0, self.T, self.N)	# time array
		C_D, A = self.problem.C_D, self.problem.A
		parachute, t_p = self.parachute, self.t_p

		# Set initial velocity
		self.v[0] = self.problem.v0 # initial velocity (m/s)

		# Check if pull time is reasonable
		if parachute:
			if t_p > self.T:
				import sys
				print "Error: t_p > T, exiting program"
				sys.exit()

		# Define area and drag coefficient as a function of time
		self.C_D = zeros(self.N)
		self.A = zeros(self.N)
		if parachute:
			F = int(ceil(t_p/self.dt)) # Number of free fall steps
			D = int(ceil(8./self.dt))  # Number of deployment steps
			
			self.A[:F] = self.problem.A
			self.A[F:F+D] = linspace(self.problem.A, self.problem.A_p, D)[:]
			self.A[F+D:] = self.problem.A_p
			
			self.C_D[:F] = self.problem.C_D
			self.C_D[F:F+D] = linspace(self.problem.C_D, self.problem.C_D_p, D)[:]
			self.C_D[F+D:] = self.problem.C_D_p
		else:
			self.C_D[:] = self.problem.C_D 
			self.A[:] = self.problem.A

		# Solve problem for t in (0, T]
		for i in range(self.N-1):
			self.step()

		return self.v, self.t


class Visualizer:
	"""Class for visualizing results, and
	calculating error"""

	def __init__(self, problem, solver):
		import matplotlib.pyplot as plt
		self.plt = plt
		self.problem, self.solver = problem, solver

	def plot(self, include_exact=False, plot=None):
		"""Plot velocity of skydiver vs time"""
		solver, problem = self.solver, self.problem
		plt = self.plt

		plt.plot(solver.t, solver.v)
		plt.xlabel(r'$t$ (s)', fontsize=16)
		plt.ylabel(r'$v$ (m/s)', fontsize=16)
		plt.title(r'Fallrate of a skydiver', fontsize=16)
		plt.grid()
		if plot:
			plt.savefig(plot + '.pdf')
		plt.show()

	def plot_error(self, plot=None):
		"""Plot error found using MMS"""
		solver, problem = self.solver, self.problem
		plt = self.plt

		error = abs(solver.v - solver.exact_solution(solver.t))
		print max(error)
		
		plt.plot(solver.t, log10(error))
		plt.xlabel(r'$t$ (s)', fontsize=16)
		plt.ylabel(r'$\log_{10}(u-u_e)$', fontsize=16)
		plt.title(r'Error using MMS', fontsize=16)
		plt.legend([r'b=%g, c=%g' % (solver.b, problem.v0)], 4)
		plt.grid()
		if plot:
			plt.savefig(plot + '.pdf')
		plt.show()

	def plot_height(self, z0=3000., plot=None):
		"""Plot height above ground vs time"""
		problem, solver = self.problem, self.solver
		plt = self.plt
		N, v, dt, t = solver.N, solver.v, solver.dt, solver.t

		z = zeros(N)
		z[0] = z0
		for i in range(N-1):
			z[i+1] = z[i] - v[i]*dt

		plt.plot(t, z)
		plt.xlabel(r'$t$ (s)', fontsize=16)
		plt.ylabel(r'$z$ (m)', fontsize=16)
		plt.title(r'Height above ground level')
		plt.grid()
		if plot:
			plt.savefig(plot + '.pdf')
		plt.show()

	def plot_forces(self, plot=None):
		"""Plot gravity and drag force vs time"""
		solver, problem = self.solver, self.problem
		plt = self.plt
		
		t = solver.t 
		g = zeros(len(t)); g[:] = problem.m*problem.g
		C_D, rho, A, v = solver.C_D, problem.rho, solver.A, solver.v
		F_d = 0.5*C_D*rho*A*abs(v)*v

		plt.plot(t, g/1000.)
		plt.plot(t, F_d/1000.)
		plt.xlabel(r'$t$ (s)', fontsize=16)
		plt.ylabel(r'Forces (kN)', fontsize=16)
		plt.title(r'Magnitude of forces', fontsize=16)
		plt.legend(['$G$', '$F_D$'], 4)
		plt.grid()
		if plot:
			plt.savefig(plot + '.pdf')
		plt.show()
		
	def plot_exact(self, plot=None):
		"""Plot the exact solution used in MMS"""
		solver, problem = self.solver, self.problem
		plt = self.plt

		plt.plot(solver.t, problem.exact_solution(solver.t))
		plt.xlabel(r'$t$ (s)', fontsize=16)
		plt.ylabel(r'$v$ (t)', fontsize=16)
		plt.title(r'Exact solution, as demanded for MMS', fontsize=16)
		plt.grid()
		if plot:
			plt.savefig(plot + '.pdf')
		plt.show()

def test_mms():
	"""Function for testing the numerical scheme
	through MMS, should reproduce linear solution
	to machine precision."""
	import nose.tools as nt
	problem = Problem(v0=3.9)
	solver = Solver(problem, dt=1e-4, b=2.3, mms=1, T=10., parachute=False)
	print "\nTesting for a linear exact solution using MMS: "
	print "v(t)=bt + c, b=%g, c=%g, dt=%.2e" % (solver.b, problem.v0, solver.dt)
	solver.solve()

	# Use L-infty norm
	diff = abs(solver.v - solver.exact_solution(solver.t)).max()
	print "Max error: %g" % diff
	delta = 1E-12
	nt.assert_almost_equal(diff, 0, delta=delta, msg='Testing MMS, v(t)=bt+c, delta=%.2e' % delta)

	# Print plot of error
	#vis = Visualizer(problem, solver)
	#vis.plot_error(plot="errorplot")

def test_convergence():
	"""Function for testing the convergence rate
	of the numerical scheme using MMS, the CR should
	be close to 2, as a CN difference is used."""
	import nose.tools as nt
	b = 2.3;  c = 3.9
	print "\nTesting Convergence Rate of Solver: "
	print "v(t) = bt + c, b=%g, c=%g" % (b, c)
	problem = Problem(v0=c)
	solver = Solver(problem, mms=2, b=b, dt=1., T=10., parachute=False)
	v, t = solver.solve()

	# Previous time step
	dtp = 1.
	# Error for previous time step, using L2-norm
	e = (v - solver.exact_solution(solver.t))**2
	error = abs(solver.v - solver.exact_solution(solver.t))

	Ep = sqrt(sum(e*dtp))
	
	for dt in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]:
		solver = Solver(problem, mms=2, b=b, dt=dt, T=10., parachute=False)
		v, t = solver.solve()

		# Calculate L2-norm for new dt
		e = (v - solver.exact_solution(solver.t))**2
		E = sqrt(sum(e*dt))

		# Compute convergence rate
		r = (log(E) - log(Ep))/(log(dt) - log(dtp))

		# Update values
		Ep = E
		dtp = dt

		# Assert using nosetools
		nt.assert_almost_equal(r, 2, places=1)

		print "dt = %6.2e, E = %8e, r = %8g" % (dt, E, r)

# Example of use and testing
if __name__ == '__main__':
	# Set up problem and solver
	problem = Problem()
	solver = Solver(problem)
	
	# Read arguments from command-line
	parser = problem.define_command_line_options()
	parser = solver.define_command_line_options(parser)
	args = parser.parse_args()
	problem.init_from_command_line(args)
	solver.init_from_command_line(args)
	
	# Set up visualizer
	vis = Visualizer(problem, solver)
	
	# Solve problem
	solver.solve()

	# Plot results
	vis.plot()
	vis.plot_height()
	vis.plot_forces()


"""
$>>> nosetests -s project1.py

Testing for a linear exact solution using MMS: 
v(t)=bt + c, b=2.3, c=3.9, dt=1.00e-04
Max error: 2.59348e-13
.
Testing Convergence Rate of Solver: 
v(t) = bt + c, b=2.3, c=3.9
dt = 1.00e-01, E = 7.624395e-04, r =  2.01564
dt = 1.00e-02, E = 7.599604e-06, r =  2.00141
dt = 1.00e-03, E = 7.597157e-08, r =  2.00014
dt = 1.00e-04, E = 7.598826e-10, r =   1.9999
dt = 1.00e-05, E = 7.535791e-12, r =  2.00362
.
----------------------------------------------------------------------
Ran 2 tests in 10.740s

OK
"""
'''