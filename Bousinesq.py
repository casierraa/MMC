# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:54:53 2015

@author: Cesar Sierra _ Juan Gomez _ Mario Saenz. Mecanica Aplicada

Title:
Porpuse: Bem  with force P
"""
# ***** References *****
import matplotlib.pyplot as plt
from numpy import sqrt, sign, arccos, cos, sin, pi,linspace,meshgrid
# ***** End *****

plt.close("all")

# ***** Define dimensions and dates *****
l = 1
P = 1
# ***** end *****

# ***** define mesh ******
nx, ny = (100, 100)
px = linspace(-l, l, nx)
py = linspace(0, 2*l, ny)
x, y = meshgrid(px, py)
r = sqrt(x**2 + y**2)                     # radio
teta = arccos(y/r) * sign(x)            # angle
# ***** end *****


# ***** tensor de esfuerzos polares *****
srr = -2.0*P / (r*pi) * cos(teta)
# ***** end *****

# ***** tensor de esfuerzos cartesianas *****
sxx = -2.0*P / (y*pi)*(cos(teta))**4
syy = -2.0*P / (y*pi) * (cos(teta))**2 *(sin(teta))**2
txy = -2.0*P / (y*pi) *(cos(teta))**3 *sin(teta)
# ***** end *****

# **** Create plots *****
# **** Tensor polar *****
fig1,plots = plt.subplots(1, 1, figsize=(22, 22))
fig1.subplots_adjust(bottom=0.1,top = 0.90,left=0.1,right=0.99,hspace = .50)
nc = 200
plt.subplot(1,1,1)
plt.title('Esfuerzo normal radial - s_rr',fontsize=30)
plt.contourf(x,y,srr,nc, alpha=.75, cmap='jet',vmin=-5.0, vmax=0.0)
plt.colorbar()
plt.grid()

subplot = plt.subplot(1,1,1)
subplot.set_xlabel('X', labelpad=30, size=25, weight='normal', family='Serif',style='normal')
subplot.set_ylabel('Profundidad', labelpad=30, size=25, weight='normal', family='Serif',style='normal')
# xticks
xticks = linspace(-l, l, 11, endpoint=True)
subplot.set_xticks(xticks)
subplot.set_xlim(-l,l)
subplot.set_xticklabels(["$%.1f$" % xv for xv in xticks], fontsize=20)
# yticks
yticks = linspace(0,2*l, 11, endpoint=True)
subplot.set_yticks(yticks)
subplot.set_yticklabels(["$%.1f$" % yv for yv in yticks], fontsize=20)
subplot.set_ylim(2*l,0)

plt.savefig('Bou_Tenrteta.pdf', dpi=72)
# ***** End *****

# **** Tensor cartesiano *****
# **** Tensor xy *****
fig1,plots = plt.subplots(2, 1, figsize=(22, 30))
fig1.subplots_adjust(bottom=0.1,top = 0.90,left=0.1,right=0.99,hspace = .20)
nc = 200
plt.subplot(2,1,1)
plt.title('Esfuerzo normal - s_xx',fontsize=30)
plt.contourf(x,y,sxx,nc, alpha=.75, cmap='jet',vmin=-5.0, vmax=0.0)
plt.colorbar()
plt.grid()
plt.subplot(2,1,2)
plt.title('Esfuerzo normal - s_yy',fontsize=30)
plt.contourf(x,y,syy,nc, alpha=.75, cmap='jet',vmin=-5.0, vmax=0.0)
plt.colorbar()
plt.grid()

# ***** Format Plots *****
for Nro in range(2):

    subplot = plt.subplot(2,1,Nro + 1)
    subplot.set_xlabel('X', labelpad=30, size=25, weight='normal', family='Serif',style='normal')
    subplot.set_ylabel('Profundidad', labelpad=30, size=25, weight='normal', family='Serif',style='normal')
    # xticks
    xticks = linspace(-l, l, 11, endpoint=True)
    subplot.set_xticks(xticks)
    subplot.set_xlim(-l,l)
    subplot.set_xticklabels(["$%.1f$" % xv for xv in xticks], fontsize=20)
    # yticks
    yticks = linspace(2*l,0, 11, endpoint=True)
    subplot.set_yticks(yticks)
    subplot.set_yticklabels(["$%.1f$" % yv for yv in yticks], fontsize=20)
    subplot.set_ylim(2*l,0)

plt.savefig('Bou_Tenxx.pdf', dpi=72)
# ***** End *****

fig1,plots = plt.subplots(1, 1, figsize=(22, 22))
fig1.subplots_adjust(bottom=0.1,top = 0.90,left=0.1,right=0.99,hspace = .50)
nc = 200
plt.subplot(1,1,1)
plt.title('Esfuerzo tangencial - t_xy',fontsize=30)
plt.contourf(x,y,txy,nc, alpha=.75, cmap='jet',vmin=-1.0, vmax=1.0)
plt.colorbar()
plt.grid()

subplot = plt.subplot(1,1,1)
subplot.set_xlabel('X', labelpad=30, size=25, weight='normal', family='Serif',style='normal')
subplot.set_ylabel('Profundidad', labelpad=30, size=25, weight='normal', family='Serif',style='normal')
# xticks
xticks = linspace(-l, l, 11, endpoint=True)
subplot.set_xticks(xticks)
subplot.set_xlim(-l,l)
subplot.set_xticklabels(["$%.1f$" % xv for xv in xticks], fontsize=20)
# yticks
yticks = linspace(0,2*l, 11, endpoint=True)
subplot.set_yticks(yticks)
subplot.set_yticklabels(["$%.1f$" % yv for yv in yticks], fontsize=20)
subplot.set_ylim(2*l,0)

plt.savefig('Bou_Tenxy.pdf', dpi=72)


print("End Proccess")

