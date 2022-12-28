fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print(x)

for x in "banana":
	print(x)

#break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print(x)
	if x == "banana":
		break
	
#if break comes before print

fruits = ["apple", "banana", "cherry"]
for x in fruits:
	if x == "banana":
		break
	print(x)	

#continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
    	continue
    print(x)

#range
for x in range(6):
	print(x)


#start parameter
for x in range(2, 6):
	print(x)

#increment the sequence
for x in range(2, 30, 3):
	print(x)

#arithmetic operators
a = 10
b = 2
print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b)

#normal division , floor division , remainder
a = 12
b = 10
print("a/b=",a/b)
print("a//b=",a//b)
print("a%b=",a%b)
print("a**b=",a**b)

#comparision operators
a = 10
b = 20
print("a > b is ", a>b)
print("a >=b is ", a>=b)
print("a < b is",a<b)
print("a<=b is",a<=b)

#assignment operators
x = 10
x+=10 #===> x = x + 10
x+=20;
print(x)
x&=5
print(x)

#identity operators
a = 10
b = 10
print(a is b)

#membership operators
x = "hello alexa"
print("h" in x)
print("d" in x)
print("d" not in x)
print("alexa" in x)


# conditional statements
name=input("enter name:")
if name=="hello":
	print("hello alexa")
else:
	print("bye alexa")
	print("are you ok")
	