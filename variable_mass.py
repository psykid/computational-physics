import matplotlib.pyplot as plt
import numpy as np
from math import sin, pi

def f(x,function):
    return eval(function)
def string__(function,ratio):
    fig, ax= plt.subplots()
    dx=0.01
    dt=0.0001
    n=100
    gamma=0
    maxtime=2
    c2=gamma*dt/dx**2
    c=100
    epsilon=(dt*c/dx)**2
    u_0=[]
    x=[]
    x+=[0]
    time=0
    du_0=[]
    u_old=[]
    u=[]
    u_new=[]
    for i in range(1,n):
        x+=[x[i-1]+dx]
    for i in range(0,n):
        if(i==0|i==n-1):
            u_0+=[0]
        else:
            u_0+=[f(x[i],function)]
        u+=[0]
        u_new+=[0]
        du_0+=[0]
    u_old=u_0
    for i in range(1,n-1):
        if i<n/2:
            eps=epsilon
        else:
            eps=epsilon/ratio #change
            #points, = ax.plot(x, u, marker='o', linestyle='--',color= 'r',markersize=3) #linestyles = ['_', '-', '--', ':']
        u[i]=float(0.5*eps*(u_0[i+1]+u_0[i-1])+(1-eps)*u_0[i]+dt*du_0[i])
    i=0
    while(time<maxtime):
        if time==0:
            points, = ax.plot(x, u, marker='o', linestyle='--',color= 'g',markersize=3) #linestyles = ['_', '-', '--', ':']
            ax.set_xlim(0,dx*n)
            ax.set_ylim(-3,3)
        else:
            for i in range(1,n-1):
                U1=u[i+1]-2*u[i]+u[i-1]
                U0=u_old[i+1]-2*u_old[i]+u_old[i-1]
                if i<n/2:
                    eps=epsilon
                else:
                    eps=epsilon/ratio #change
                    #points, = ax.plot(x, u, marker='o', linestyle='--',color= 'r',markersize=3) #linestyles = ['_', '-', '--', ':']
                u_new[i]=eps*U1+2*u[i]-u_old[i]+c2*(U1-U0)
            for i in range(0,n):
                u_old[i]=u[i]
                u[i]=u_new[i]
            points.set_data(x,u_new)
        time+=dt
        plt.pause(0.00005)

#string__("2.71**(-1*100*(x-0.2)**2)",100)
