print("condition is true")
a = 5
b = 4
c = 1

if a>b and a>c:
	print("a is big")
elif b>c:
   print("b is big")
else:
   print("c is big")

# nested blocks
print("aaaaaaaaaaaaaaaaaaaaa")
if a > b:
	if a>c:
		print("a is biggest")
		if a==2:
			print("a is 2")


PI = 3.14
print(PI)

PI = 2
print(PI)
print(type(PI))

fruits = ["apple", "banana", "cherry"]
for y in fruits:
	print(y)



	#break
fruits = ["apple", "banana", "cherry"]
for y in fruits:
	print(y)
	if y == "banana":
		break


	#if break comes before print

	fruits = ["apple", "banana", "cherry"]
for x in fruits:
	if x == "banana":
		break
print(y)	

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
	print(y)

	#increment the sequence
	for x in range(2, 30, 3):
		print(x)

a = 2
if a==1:
	print("happy")
else:
	print("this is false block")




a = 20
b = 30
c = 40
if a > b and a > c:
	print("a is big")
elif b>c:
	print("b is big")
else:	
	print("c is big")



	 # nested blocks
print("aaaaaaaaaaaaaaaaaaaaa")
if a > b:
	if a>c:
		print("a is biggest")
		if a==2:
			print(",,,,,,,,,,,,,,,")



a = 5
b = 5
if a > b:
  print("a is big")
  print("this is true")

if a > b:
  	print("a is big")
  	print("no cond is true")

a = 2
if a==1:
	print("happy")
else:
	print("this is false block")




a = 20
b = 30
c = 40
if a > b and a > c:
	print("a is big")
elif b>c:
	print("b is big")
else:	
	print("c is big")



	 # nested blocks
print("aaaaaaaaaaaaaaaaaaaaa")
if a > b:
	if a>c:
		print("a is biggest")
		if a==2:
			print(",,,,,,,,,,,,,,,")



a = 5
b = 5
if a > b:
  print("a is big")
  print("this is true")

if a > b:
  	print("a is big")
  	print("no cond is true")

if a==1:
  print("todays happiness")
else:
	print("this is flase block")


slice
n=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[2:7:2])
print(n[4::2])
print(n[3:7])
print(n[8:2:-2])
print(n[4:100])


#mutability
n = [10, 20, 30, 40]
print(n)
n[1]=777
print(n)

 = " happy new year"
print("h" in x)
print("d" in x)
print("d" not in x)
print("alexa" in x)



name=input("enter name:")
if name=="new year":
	print("happy new year")
else:
	print("bye 2022")
	print("welcome to 2023")
	