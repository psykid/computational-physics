from sympy import *
from math import *
import math

x=Symbol('x')

def f(x,fun):
    return eval(fun)

def g(x,p,fun):
    y=x
    x=Symbol('x')
    der= diff(fun,x,p)
    x=y
    return 1.0*(eval(str(der)))

#fun="1/x"
def maclauren__(fun,a,b):
    h=0.1
    #a=1
    #b=2
    n=2
    num=int((b-a)/h)

    coeff=[]
    for i in range(1,n+1):
        dummy=bernoulli(2*i)/math.factorial(2*i)
        coeff+=[dummy]

    y=[]
    k=int((b-a)/h)
    for i in range (0,k+1):
            y+=[a+i*h]
    sum1=0

    for j in range(1,k):
            sum1+=f(y[j],fun)*h	

    sum2=(f(y[0],fun)+f(y[k],fun))*h/2

    summ=sum1+sum2
    sum2=0
    #print 'from trapezoid rule :/', summ
    #print g(b,b)
    for i in range(0,len(coeff)):
        sum1=float(coeff[i]*(g(a,2*i+1,fun)-g(b,2*i+1,fun))*h**(2*i+2))
        sum2+=sum1

    return sum2+summ

hal=maclauren__("1/x",1,2)
print hal
