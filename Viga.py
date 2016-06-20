# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:54:53 2015

@author: Cesar Sierra _ Juan Gomez _ Mario Saenz. Mecanica Aplicada

Title:
Porpuse: Bem  with force P
"""
# ***** References *****
import matplotlib.pyplot as plt
from numpy import linspace,meshgrid,sqrt
# ***** End *****

plt.close("all")

# ***** Define dimensions and dates *****
l= 5.0									# Lenght
h= 1.0									# hight
b= 1.0									#
I = 1.0/12.0*2.0*b*(2.0*h)**3		    # Inertia
P = 1                                  # Force
# ***** end *****

# ***** define mesh ******
nx, ny = (100*l, 100)
px = linspace(0, l, nx)
py = linspace(-h, h, ny)
x, y = meshgrid(px, py)
# ***** end *****

# ***** tensor de esfuerzos *****
sxx=-P/I*x*y
syy= 0.0*x
txy= -P/(2.0*I)*(h**2 - y**2);
# ***** end *****

# ***** tensor en direcciones principales *****
cx = (sxx + syy)/2.0
tmax = sqrt((sxx - cx)**2 + txy**2)
smax = cx + tmax
smin = cx - tmax
# **** end ****

# **** Create plots *****
# **** Tensor xy *****
fig1,plots = plt.subplots(2, 1, figsize=(22, 26))
fig1.subplots_adjust(bottom=0.1,top = 0.90,left=0.1,right=0.99,hspace = .50)
nc = 50
plt.subplot(2,1,1)
plt.title('Esfuerzo normal - s_xx',fontsize=30)
plt.contourf(x,y,sxx,nc, alpha=.75, cmap='jet')
plt.colorbar()
plt.grid()
plt.subplot(2,1,2)
plt.title('Esfuerzo cortante t_xy',fontsize=30)
plt.contourf(x,y,txy,nc, alpha=.75, cmap='jet')
plt.colorbar()
plt.grid()

# ***** Format Plots *****
for Nro in range(2):

    subplot = plt.subplot(2,1,Nro + 1)
    subplot.set_xlabel('Longitud', labelpad=30, size=25, weight='normal', family='Serif',style='normal')
    subplot.set_ylabel('Altura', labelpad=30, size=25, weight='normal', family='Serif',style='normal')
    # xticks
    xticks = linspace(0.0, l, 5, endpoint=True)
    subplot.set_xticks(xticks)
    subplot.set_xlim(0.0,l)
    subplot.set_xticklabels(["$%.1f$" % xv for xv in xticks], fontsize=20)
    # yticks
    yticks = linspace(-h, h, 5, endpoint=True)
    subplot.set_yticks(yticks)
    subplot.set_yticklabels(["$%.1f$" % yv for yv in yticks], fontsize=20)
    subplot.set_ylim(h,-h)

plt.savefig('Viga_Tenxy.pdf', dpi=72)
# ***** End *****

# # **** Tensor principal *****
fig2,plots2 = plt.subplots(3, 1, figsize=(22, 26))
fig2.subplots_adjust(bottom=0.1,top = 0.90,left=0.1,right=0.99,hspace = .50)
nc = 50
plt.subplot(3,1,1)
plt.title('Esfuerzo normal maximo - s_max',fontsize=30)
plt.contourf(x,y,smax,nc, alpha=.75, cmap='jet')
plt.colorbar()
plt.grid()
plt.subplot(3,1,2)
plt.title('Esfuerzo normal minimo - s_max',fontsize=30)
plt.contourf(x,y,smin,nc, alpha=.75, cmap='jet')
plt.colorbar()
plt.grid()
plt.subplot(3,1,3)
plt.title('corte maximo - t_max',fontsize=30)
plt.contourf(x,y,tmax,nc, alpha=.75, cmap='jet')
plt.colorbar()
plt.grid()

# ***** Format Plots *****
for Nro in range(3):

    subplot = plt.subplot(3,1,Nro + 1)
    subplot.set_xlabel('Longitud', labelpad=30, size=25, weight='normal', family='Serif',style='normal')
    subplot.set_ylabel('Altura', labelpad=30, size=25, weight='normal', family='Serif',style='normal')
    # xticks
    xticks = linspace(0.0, l, 5, endpoint=True)
    subplot.set_xticks(xticks)
    subplot.set_xlim(0.0,l)
    subplot.set_xticklabels(["$%.1f$" % xv for xv in xticks], fontsize=20)
    # yticks
    yticks = linspace(-h, h, 5, endpoint=True)
    subplot.set_yticks(yticks)
    subplot.set_yticklabels(["$%.1f$" % yv for yv in yticks], fontsize=20)
    subplot.set_ylim(h,-h)
plt.savefig('Viga_Tenprin.pdf', dpi=72)
# # ***** End *****
print("End Proccess")


