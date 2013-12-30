import math
import numpy as np

fun="1.0/x"
lb, ub=1, 2
def f(x):
	return eval(fun)

def T(m,k):
	if k==0:
		return T_0(m)
	
	return

def T_0(m):
	N=2**m
	step=(ub-lb)*1.0/N
	i, summ=lb+step,0
	while i<ub:
		summ+=f(i)
		i+=step
	summ+=0.5*(f(lb)+f(ub))
	return summ*step	
	
#0.69314718055994529
def main():
	#_n=int(raw_input("enter k, for degree of accuracy h^2k: "))
	#_m=int(raw_input("enter initial m, for 2^m starting points: "))
	_k=5
	_m=3
	
	T=np.zeros((_k+1,_k+1))
	
	for m in range(_k+1):
		for k in range(m+1):
			print m,k
			if k==0:
				T[m][k]=T_0(_m+m)
				continue
			T[m][k]=((2**(2*k))*T[m,k-1]-T[m-1,k-1])/(2**(2*k)-1)
			
	print T
		
main()

