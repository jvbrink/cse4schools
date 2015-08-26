
.. sagecellserver:: python

    from pylab import *
    
    """Declaring all the paramters we need"""
    m = 90 #kg, mass of the jumper
    g = 9.81 #m/s**2, the gravitational acceleration
    rho = 1 #kg/m**3, air density
    A = 0.7 #m**2, area covered by the parachute 
    C = 1.4 #drag coefficient
    A_p = 44 #m**2, area covered by the parachute when deployed
    C_p = 1.8 #drag coefficient when the parachute is deployed
    v0 = 0 #m/s, the initial velocity
.. sagecellserver:: python

    """Defining the acceleration as a function of the velocity"""
    def a(v):
        return g - 0.5*rho*C*A/m*v*v
.. sagecellserver:: python

    """Defining the values need to create the time array"""
    dt = 0.01
    T = 180
    n = int(T/dt)
.. sagecellserver:: python

    """Declaring three arrays, one for the velocity v, one for the time t and one for 
    the gravitational forces."""
    t = zeros(n+1)
    v = zeros(n+1)
    gforces = zeros(n+1)
.. sagecellserver:: python

    # Simulating the first 60 seconds
    """A for loop calculating the velocity for the free fall and updating the time"""
    for i in range(0, int(60/dt)):
        t[i+1] = t[i] + dt
        v[i+1] = v[i] + a(v[i])*dt
        gforces[i] = 1 - a(v[i])/g
.. sagecellserver:: python

    # Simulating the next 5 seconds
    """A for loop calculating the velocity while the parachute is deploying """
    for i in range(int(60/dt), int(65/dt)):
        C += (C_p-C)/(5/dt) 
        A += (A_p-A)/(5/dt)
    
        t[i+1] = t[i] + dt
        v[i+1] = v[i] + a(v[i])*dt
        gforces[i] = 1 - a(v[i])/g
.. sagecellserver:: python

    # Simulating the last 120 seconds
    """A for loop calculating the velocity while the parachute is deployed"""
    for i in range(int(65/dt), int(180/dt)):
        t[i+1] = t[i] + dt
        v[i+1] = v[i] + a(v[i])*dt
        gforces[i] = 1 - a(v[i])/g
.. sagecellserver:: python

    """Ploting the velocity throughout the jump"""
    %matplotlib inline
    plot(t,v)
    xlabel('t')
    ylabel('v(t)')
    grid()


.. image:: output_7_0.png


.. sagecellserver:: python

    """Ploting the g forces experienced by the jumper"""
    plot(t,gforces)
    xlabel('t')
    ylabel('gforces')
    grid()
    show()


.. image:: output_8_0.png


