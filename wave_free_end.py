import matplotlib.pyplot as plt
import numpy as np
from math import sin,pi

def f(x,function):
        return eval(function)

def string__(n,function):
	fig, ax = plt.subplots()
	#n=input("enter the size of N: ")
	#maxtime=input("enter the max time: ")
	dx=0.01#dx
	dt=0.0001
	#print 'hello'
	gamma=0
	c2 = gamma*dt / dx**2
	c=100
	epsilon = (dt*c/dx)**2
	maxtime=2
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
		if(i==0):#|i==n-1):
			u_0+=[0]
		else:
			#u_0+=[2.71**(-1*100*(x[i]-0.2)**2)]
			u_0+=[f(x[i],function)]
			#u_0+=[0]
		u+=[0]
		u_new+=[0]
		du_0+=[0]
	u_old=u_0
	#u=u_0
	#u_0[20]=-1
	#u_old[20]=-1
	for i in range(1,n-1):
		u[i]=float(0.5*epsilon*(u_0[i+1]+u_0[i-1])+(1-epsilon)*u_0[i]+dt*du_0[i])
	u_dum=u
	i=0
	while (time<maxtime):
		if time == 0:
			points, = ax.plot(x, u, marker='o', linestyle='None')
			ax.set_xlim(0, 1)
			ax.set_ylim(-3, 3)
		else:
			for i in range (1, n-1):
				U1 = u[i+1] - 2*u[i] + u[i-1]
				U0 = u_old[i+1] - 2*u_old[i] + u_old[i-1]
				u_new[i] = epsilon*U1 + 2.0*u[i] - u_old[i] + c2*(U1-U0)
			u_new[i]=u_new[i-1]
			u_new[n-1]=u_new[i-1]
			for i in range (0, n):
				u_old[i] = u[i]
				u[i] = u_new[i]
			points.set_data(x,u_new)
		time+=dt
		plt.pause(0.00005)

#string__(100,"sin(x*2.5*pi)")
