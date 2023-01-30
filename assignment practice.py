#bubble sort
def bs(a):
	#b = len(a)- 2nbsp;
	for x in range(b):
		for y in range(b-x):
			a[y]=a[y+1]
	a=[32,5.3,6,7,54,87]
	bs(a)		

	#to produce star traingle
def pyfunc(r):
	for x in range(r):
		print(''*(r-x-1)+'*'*(2*x+1))
		pyfunc(9)

# fibonacci series
a = int(input("enter the terms"))
f=0;
s=1
if a==0:
	print("the requested series is",f)
else:
	print(f,s,end="")
	for i in range(2,a):
		print(next,end="")
		f=b
		s=next

#check number is prime 

a= int(input("enter the number"))
if a!=1:
	for x in range(2,a):
		if(a%x)==0:
			print("not prime")
			break
		else:
			print("prime")
else:
	print("not prime")


