from sympy import *
from math import *


x1= Symbol('x1')
x2=Symbol('x2')

#fun1=raw_input("enter a first function: ")
#fun2=raw_input("enter a second function: ")
fun1=x2-2*x1
fun2=x1-2*x2
#x10= float(input("enter the x10(first_variable): "))
x10=0.1
x20=0.1
#x20= float(input("enter the x20(second_variable): "))
#v10= float(input("enter the v1(start point): "))
#v20= float(input("enter the v2(start point): "))
h=0.05
#h= float(input("enter the h: "))
v20=0
v10=0


def f2(x1,x2):
    return eval(str(fun2))


def f1(x1,x2):
    return eval(str(fun1))

ans=[]
f = open('myfile.txt','w')
def oscillator(time):
    t1=0
    global v10
    global v20
    global h
    global x10
    global x20
    num= int((time-t1)/h)
    t=[]
    
    

    for i in range(0,num+1):
        t=t+[t1+i*(h)]

    x1_nw=0
    x2_nw=0
    v1=v10
    v2=v20
    x2=x20
    x1=x10
    for j in range(0,num+1):
        v1_new=v1+h*f1(x1+((1)*h/2)*f1(x1,x2),x2+((1)*h/2)*f2(x1,x2))
        v2_new=v2+h*f2(x1+((1)*h/2)*f1(x1,x2),x2+((1)*h/2)*f2(x1,x2))
        x1_nw=x1+h*(v1_new)
        x2_nw=x2+h*(v2_new)
        f.write(str(t[j])+' '+str(x1)+'\n')
        x2=x2_nw
        x1=x1_nw
        v2=v2_new
        v1=v1_new
	
    #print time,x1_nw, x2_nw
    
    
    
    
    
    return x1_nw,x2_nw
   

ink=int(50/h)
kites=0
print 'final7',oscillator(6.283185*7)

f.close()
