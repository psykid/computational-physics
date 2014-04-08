from sympy import *
from math import *
import math

fun="1/x"
h=0.1
a=1
b=2
n=2
num=int((b-a)/h)

def f(x):
    return eval(fun)


def g(x,p):
    global fun
    der= fun
    for q in range(0,p):
        t=diff(der)
        der=t
    print ((der)).evalf(2)," dafa"
    return 1.0*(eval(str(der)))

#print bernoulli(2)
coeff=[]
for i in range(1,n+1):
    dummy=bernoulli(2*i)/math.factorial(2*i)
    print math.factorial(2*i)
    coeff+=[dummy]

print coeff
y=[]
k=int((b-a)/h)
for i in range (0,k+1):
	y+=[a+i*h]
#print x
sum1=0

for j in range(1,k):
	sum1+=f(y[j])*h	

sum2=(f(y[0])+f(y[k]))*h/2

summ=sum1+sum2
sum2=0
print 'from trapezoid rule :/', summ
#print g(b,b)
for i in range(0,len(coeff)):
    #print coeff[i]
    sum1=float(coeff[i]*(g(a,2*i+1)-g(b,2*i+1))*h**(2*i+2))
    print (g(a,2*i+1)-g(b,2*i+1)),"from diff,i ", i
    print h**(2*i+1)," from h"
    print sum1," from sum1 i ",i
    sum2+=sum1

#print g(3,1)
#print float(g(10,1))
print sum2
x=Symbol('x')
z=diff(diff("x**2"))
def f1(x):
    return float(eval(str(z)))
print f1(3),f1(2)," from f1,3,2"
print float(1/(2**4))
