# Author: Martin Luther Bironga
# Date: 24/1/2021

# problem statement
"""
create a function called persistence that finds the multiplicative persistence of 
a number that is multiplies the digits of the result until the length of the 
result becomes one digit. 
"""

from functools import reduce

def persistence(n,num=0):
	if len(str(n))==1:
		return num
	n_=[int(i) for i in str(n)]
	result=reduce(lambda x, y:x*y,n_)
	num=num+1
	return persistence(result,num)
