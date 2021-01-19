# Author: Martin Luther Bironga
# Purpose: To create a function that 
# is able to dynamically solve linear systems of 
# equations
# Date:19/01/2021

# first we get the two lists and store them in variables
a=[[1,1,2],[2,4,-3],[3,6,-5]]
b=[[9],[1],[0]]

# important variables needed for elementary operations
length=len(a)

# there are four operations that are repetitive
for j in range(length):
	if j==0:
		element=0
		continue
	a[element],b[element]=[(1/a[element][element]*num) for num in a[element]],[(1/a[element][element]*num) for num in b[element]]
	factor=a[j][element]
	temp,temp_=[-(num*factor) for num in a[element]],[-(num*factor) for num in b[element]]
	a[j],b[j]=[x+y for x,y in zip(temp,a[j])],[x+y for x,y in zip(temp_,b[j])]

print(a,b)
print("solution to linear systems")
