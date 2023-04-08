#16. Write a Python program to print the index of the character in a string.
#input=H1e2l3l4o5,o/p=Hello
print("Please enter text to print::")
inputchars = input()

if inputchars:
	string = ""
	for i in inputchars:
		if inputchars.index(i)%2 == 0:
			string += str(i)
	
	print('-------------------')
	print("You Entered:", inputchars)
	print("Result:")
	print(string)
