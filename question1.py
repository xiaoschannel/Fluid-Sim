import sys
import numpy as np
import matplotlib.pyplot as plt

nx=5
L=0.5
k=1000
TA=100
TB=500
A=10E-3
dx=L/float(nx)

x=np.zeros(nx)
for i in xrange(nx):
    x[i]=dx*(float(i)+0.5)

amat=np.zeros([nx,nx])
b=np.zeros(nx)

for i in xrange(1, nx-1):
    aw=ae=k/dx*A
    ap=aw+ae
    amat[i,i-1]=-aw
    amat[i,i]=ap
    amat[i,i+1]=-ae
    b[i]=0

aw=0
ae=k/dx*A
Sp=-2*k*A/dx
Su=2*k*A/dx*TA
ap=aw+ae-Sp

amat[0,0]=ap
amat[0,1]=-ae
b[0]=Su

aw=k*A/dx
ae=0
Sp=-2*k*A/dx
Su=2*k*A/dx*TB
ap=aw+ae-Sp

amat[nx-1,nx-2]=-aw
amat[nx-1,nx-1]=ap
b[nx-1]=Su

print amat
print b

T=np.linalg.solve(amat,b)
print T

Texact = np.zeros(nx)
for i in xrange(nx):
    x[i]=dx*(float(i)+0.5)
    Texact[i]=TA+(TB-TA)/L*x[i]
print Texact

fig=plt.figure()
plt.plot(x,T)
plt.plot(x,Texact,"*")

plt.xlim(0,L)

plt.savefig('main.png')
