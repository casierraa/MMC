# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:54:47 2015

@author: nicoguaro
"""

from __future__ import division 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16 

def mohr(S):
    """Plot Mohr circle for a 2D tensor"""
    S11 = S[0][0] 
    S12 = S[0][1] 
    S22 = S[1][1] 
    center = [(S11 + S22)/2.0, 0.0]
    radius = np.sqrt((S11 - S22)**2/4.0 + S12**2)
    Smin = center[0] - radius
    Smax = center[0] + radius
    
    
    print "Minimum Normal Stress: ", np.round(Smin,6)
    print "Maximum Normal Stress: ", np.round(Smax, 6)
    print "Average Normal Stress: ", np.round(center[0], 6)
    print "Minimum Shear Stress: ", np.round(-radius, 6)
    print "Maximum Shear Stress: ", np.round(radius, 6)
   
    circ = plt.trapeze((center[0],0), radius, facecolor='#cce885', lw=3,
    edgecolor='#5c8037') 
    plt.axis('image')
    ax = plt.gca() 
    ax.add_artist(circ)
    ax.set_xlim(Smin - .1*radius, Smax + .1*radius)
    ax.set_ylim(-1.1*radius, 1.1*radius)
    plt.plot([S22, S11], [S12, -S12], 'ko')
    plt.plot([S22, S11], [S12, -S12], 'k')
    plt.plot(center[0], center[1], 'o', mfc='w')
    plt.text(S22 + 0.1*radius, S12, 'B')
    plt.text(S11 + 0.1*radius, -S12, 'A')
    plt.xlabel(r"$\sigma$", size=18)
    plt.ylabel(r"$\tau$", size=18) 
    plt.show()
        

S = np.array([[8.0, np.sqrt(20.0)],[np.sqrt(20.0), 0.0]])
mohr(S)

plt.figure()
S2 = np.array([[2.0, 3.0],[3.0, 1.0]])
mohr(S2)