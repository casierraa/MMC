# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:00:53 2015

@author: viviana
"""

import numpy as np
import matplotlib.pyplot as plt 
from subprocess import call
import matplotlib.cm as cm
       
d=0.1
H=1.
ga=1.  

npx=int(round(H/d)+1)

X=np.zeros([npx,npx],dtype=np.float)
Y=np.zeros([npx,npx],dtype=np.float)
sigmx=np.zeros([npx,npx],dtype=np.float)
sigmy=np.zeros([npx,npx],dtype=np.float)
tauxy=np.zeros([npx,npx],dtype=np.float)
sigmac=np.zeros([npx,npx],dtype=np.float)


vx=np.linspace(0,H,npx)
vy=vx

corx=0.
cory=0.

for ix in range(npx):
    for iy in range(npx):
        
        X[ix,iy]=corx
        Y[ix,iy]=cory
        
        if(cory==corx):
            break
        cory=cory+d
    corx=corx+d
    cory=0.
 
for ix in range(npx):
    for iy in range(npx):
        corx=X[ix,iy]
        cory=Y[ix,iy]
        sigmx[ix,iy]= corx*ga-cory*ga*2.
        sigmy[ix,iy]= -corx*ga
        tauxy[ix,iy]= -cory*ga
#
for ix in range(npx):
    for iy in range(npx):
        corx=X[ix,iy]
        cory=Y[ix,iy]
        sigx= corx*ga-cory*ga*2.
        sigy= -corx*ga
        sigmac[ix,iy]= (sigx-sigy)/2        
#       
plt.figure()
CS=plt.contour(X,Y,sigmx,20)
plt.clabel(CS, inline=1, fontsize=10)
plt.plot(vx,vy,linewidth = 2.0)
plt.title('Sigma x')
plt. xlabel('x-axis')
plt. ylabel('y-axis')
#plt.show()
plt.savefig('sigmax.pdf')    

plt.figure()
CS=plt.contour(X,Y,sigmy,20)
plt.clabel(CS, inline=1, fontsize=10)
plt.plot(vx,vy,linewidth = 2.0)
plt.title('Sigma y')
plt. xlabel('x-axis')
plt. ylabel('y-axis')
#plt.show()   
plt.savefig('sigmay.pdf')

plt.figure()
CS=plt.contour(X,Y,tauxy,20)
plt.clabel(CS, inline=1, fontsize=10)
plt.plot(vx,vy,linewidth = 2.0)
plt.title('Tau xy')
plt. xlabel('x-axis')
plt. ylabel('y-axis')
#plt.show()
plt.savefig('taoxy.pdf')
#
plt.figure()
CS=plt.contour(X,Y,sigmac,20)
plt.clabel(CS, inline=1, fontsize=10)
plt.plot(vx,vy,linewidth = 2.0)
plt.title('Tao max')
plt. xlabel('x-axis')
plt. ylabel('y-axis')
#plt.show()
plt.savefig('sigmac.pdf')
#    

