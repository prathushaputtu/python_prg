text = ("i am good")#input("enter a string:")
alpha = ("o") #input("enter an alphabet:")
count=0
for x in text:
	if x == alpha:
		count+=1
print("no of times",alpha,"appears in the string",count)