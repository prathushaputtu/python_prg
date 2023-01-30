
# Program for hcf/gcd factors
def hcf(divisor, dividend)
	rem= dividend%divisor
	if rem==0:
		return divisor
	return hcf(divisor,rem)

a = int(input("enter the number "))
b= int(input ("enter the number"))
c= hcf(a,b)
print("hcf of ",a," and ",b," is ",c)


