# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 17:52:42 2015
Principal stresses for 3D sates
@author: eafit
"""
#
import numpy as np
from scipy import linalg
#
# Stress tensor
#
S = np.array([
    [18.,0,24.],
    [0,-50.,0],
    [24,0,32.]])
#
print
print "Stress invariants"
print
IS   = S[0,0]+S[1,1]+S[2,2]
IIS  =S[0,0]*S[1,1]+S[1,1]*S[2,2]+S[0,0]*S[2,2]-(S[0,1]**2)-(S[0,2]**2)-(S[1,2]**2)
IIIS =S[0,0]*S[1,1]*S[2,2]-S[0,0]*(S[1,2]**2)-S[1,1]*(S[0,2]**2)-S[2,2]*(S[0,1]**2)+2*S[1,2]*S[0,2]*S[0,1]
print IS,IIS,IIIS
#
print
print "Solution via characteristic equation"
coeff=[1.0,-IS,IIS,-IIIS]
ps=np.roots(coeff)
print
print "Principal stresses", ps
#
# Solves the eigenvalue problem using linalg library
#
print
print "Solution via library"
print
la, v= linalg.eig(S)
la=la.real
print "principal stresses", la
print
print "principal directions_ by Columns"
print
print v
print
print "Diagonalized tensor"
print
S = np.array([
    [la[0],0,0],
    [0,la[1],0],
    [0,0,la[2]]])
print S
print "Stress invariants"
IS   = S[0,0]+S[1,1]+S[2,2]
IIS  = S[0,0]*S[1,1]+S[1,1]*S[2,2]+S[0,0]*S[2,2]-(S[0,1]**2)-(S[0,2]**2)-(S[1,2]**2)
IIIS = S[0,0]*S[1,1]*S[2,2]-S[0,0]*(S[1,2]**2)-S[1,1]*(S[0,2]**2)-S[2,2]*(S[0,1]**2)+2*S[1,2]*S[0,2]*S[0,1]
print IS,IIS,IIIS



