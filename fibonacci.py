a=14#int(input("enter the terms"))

f=0
s=1
if a==0:
	print("the requested series is",f)
else:
	print(f,s,end=" ")
	for x in range(2,a):
		print(next,end=" ")
		f = s
		s = next

