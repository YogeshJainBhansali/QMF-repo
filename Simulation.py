import matplotlib.pyplot as pyplot
import numpy as np
a=0.70
q=0.23
mass_con=1/(6.023e26)
r0=(250e-6)/1.148
ome=2*np.pi*6e6
e=1.602e-19
x=[]
for i in range(1,101):
    m=i*mass_con
    u=(a/2)*(m*r0*r0*ome*ome)/(4*e)
    v=(q)*(m*r0*r0*ome*ome)/(4*e)
    x.append([round(u,3),round(v,3)])

for j in range(99):
    print((j+1),"=",x[j])
    #print("delu",x[j+1][0]-x[j][0])
    #print("del v",x[j+1][1]-x[j][1])
    
print("change in DC volate",x[3+1][0]-x[3][0])
print("change in AC voltage",x[3+1][1]-x[3][1])

#np.savetxt("RequiredVoltages.txt",x)