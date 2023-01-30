a = 23
print(a)
print(a + 2)
print(a - 3)

a = 10;
b = 2 ;
print('a+b=',a+b)
print('a-b=',a-b)
print('a*b=',a*b)
print('a/b=',a/b)
print('a//b=',a//b)
print('a%b=',a%b)
print('a**b=',a**b)

list = [3,7,5,8,4,9]
max = list[0]
for number in list:
   if(number > max):
   	max = number

print("max:", max)



list = [3,7,5,8,4,9]
min = list[0]
for number in list:
	if(number < min):
	   min = number

print("min:", min)