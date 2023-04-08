# 2. Write a Python program to count the number of characters (character frequency) in a string. 
#an example string:you only live once
#expected outcome-{'y': 2, 'o': 3, 'u': 1, ' ': 3, 'n': 2, 'l': 2, 'i': 1, 'v': 1, 'e': 2, 'c': 1}
str = input('Enter the string:\n')
counter = {}
for s in str:
    if s in counter:
        counter[s]+=1
    else:
        counter[s]=1

print(counter)