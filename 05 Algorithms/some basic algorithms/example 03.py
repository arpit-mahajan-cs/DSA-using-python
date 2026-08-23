

import functools


def fun_version1(L):
	s=0
	for i in L:
		s=s+i
	return s

def fun_version2(L):
	return sum(L)

def fun_version3(L):
	return functools.reduce(lambda i,j:i+j,L)

L = [11,22,33,44,55]
print(fun_version1(L)) 
print(fun_version2(L))
print(fun_version3(L)) 