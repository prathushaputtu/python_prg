sentence=(" i am not good")      #int(input("enter the sentence"))
string = sentence.lower()
print(string)
count=0
list1=["a","e","i","o","u"]
for char in string:
	if char in list1:
		count = count+1
print("number vowels is given sentence" ,count+1)