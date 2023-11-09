import matplotlib.pyplot as plt
import numpy as np
m= 100/(6.023e26) #mass in kg
r0=(500e-6)/1.148 #radius of hyperbolic feild
ome=2*np.pi*6e6 #Angular Velocity of the applied AC voltage
e=1.602e-19 #Charge of 1 electron
a=0.2 # Value of a decided to run the computaion
q=0.61 # Value of q decided to run the computaion
dc=(a/2)*(m*r0*r0*ome*ome)/(4*e) #DC voltage
ac=(q)*(m*r0*r0*ome*ome)/(4*e) #AC voltage
print (dc,ac)

# Function to return the values of change in velocity along X axis
#def u_(t,x,u):
   # return((-2*e*(dc+ac*np.cos(ome*t))*x)/(m*r0*r0))

# Function to return the values of change in velocity along Y axis
def u_(t,y,v):
    return((2*e*(dc+ac*np.cos(ome*t))*y)/(m*r0*r0))

Length=30e-3 #Length of the QMF rods
vz=np.sqrt((2*e*5)/m) # Velocity of the ions along the Z axis when they enter the feild 
Tf=Length/vz # total time it takes for ions to reach the other end of rod

#below are the inital parameter for position and velocity along X and Y axis
x0=1e-6
y0=1e-6
u0=0
v0=0
t0=0

step_size=1/((6e6)*40)
no_steps=np.ceil(Tf/step_size)
xmotion=[]
time=[]
r1=[]
r2=[]

#Function using range-kutta 4th order method to solve 2nd order differnetial equation
def rangekutta(x,u,t):
    for i in range(int(no_steps)):
        xmotion.append(x)
        time.append(t)
        r1.append(r0)
        r2.append(-r0)
        t=t+step_size
        l1=step_size*u_(t,x,u)
        k1=step_size*u
        l2=step_size*u_((t+ step_size/2),(x+ k1/2),(u+ l1/2))
        k2=step_size*(u+l1/2)
        l3=step_size*u_((t+ step_size/2),(x+ k2/2),(u+ l2/2))
        k3=step_size*(u+ l2/2)
        l4=step_size*u_((t+ step_size),(x+ k3),(u+ l3))
        k4=step_size*(u+l3)
        l=(l1+2*l2+2*l3+l4)/6
        k=(k1+2*k2+2*k3+k4)/6
        x=x+k
        u=u+l
    #Printing values of motion of ions at each individual time jump  
    #print(xmotion)
    #print(time)
    plt.plot(time,xmotion)
    plt.plot([0,Tf],[0,0],'r--')
    #plt.plot(time,r1)
    #plt.plot(time,r2, color='orange')
    #plt.ylim(-r0*1.1,r0*1.1)
    plt.xlabel('Time in sec x 10^(-5)')
    #plt.ylabel('postion along the X-Z plane in micro-meters')
    plt.ylabel('postion along the Y-Z plane in meters')
    plt.show()
    print("The orange line in the graph are the rods where the ions will get discharged")
    
rangekutta(x0,u0,t0)