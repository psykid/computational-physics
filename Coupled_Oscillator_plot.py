import matplotlib.pylab as plt
from sympy import *
from math import *


x1= Symbol('x1')
x2=Symbol('x2')

###fun1=raw_input("enter a first function: ")
###fun2=raw_input("enter a second function: ")
##fun1=x2-2*x1
##fun2=x1-2*x2
###x10= float(input("enter the x10(first_variable): "))
##x10=0.1
##x20=0.1
###x20= float(input("enter the x20(second_variable): "))
###v10= float(input("enter the v1(start point): "))
###v20= float(input("enter the v2(start point): "))
##h=0.05
###h= float(input("enter the h: "))
##v20=0
##v10=0

def plot_data():
    datalist = [ ( plt.loadtxt("myfile.txt"), "label")]

    for data, label in datalist:
        plt.plot( data[:,0], data[:,1], label=label )

    plt.legend()
    plt.title("Plot of coupled oscillator")
    plt.xlabel("Time")
    plt.ylabel("Position")
    plt.show()
    plt.pause(0.000005)


def f2(fun2,x1,x2):
    return eval(str(fun2))


def f1(fun1,x1,x2):
    return eval(str(fun1))

ans=[]
f = open('myfile.txt','w')
def oscillator(fun1,fun2,x10,x20,h,v10,v20,time):
    #global fun1,fun2
    t1=0
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
        v1_new=v1+h*f1(fun1,x1+((1)*h/2)*f1(fun1,x1,x2),x2+((1)*h/2)*f2(fun2,x1,x2))
        v2_new=v2+h*f2(fun2,x1+((1)*h/2)*f1(fun1,x1,x2),x2+((1)*h/2)*f2(fun2,x1,x2))
        x1_nw=x1+h*(v1_new)
        x2_nw=x2+h*(v2_new)
        f.write(str(t[j])+' '+str(x1)+'\n')
        x2=x2_nw
        x1=x1_nw
        v2=v2_new
        v1=v1_new

    #print time,x1_nw, x2_nw
    f.close()

    plot_data()
    return x1_nw,x2_nw

#oscillator(x2-2*x1,x1-2*x2,0.1,0.1,0.05,0,0,6.283185*2)
#oscillator(fun1,fun2,x10,x20,h,v10,v20,time):
