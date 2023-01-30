# program to know the factorial for number
# number = input("enter the number:\n")
# print(number)
number = 5
factorial=1
if (number<=0):
	print("can't compute factorial for negative number")
elif(number<2):
	print(factorial)
else:
	for number in range(number,1,-1):
		factorial=factorial*number
print(factorial)
 
