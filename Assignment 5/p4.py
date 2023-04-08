# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'excuse'
# Expected Result : 'excus$'
str = input("Enter the string:\n")
isr = False
finalString = ''
for s in str:
    if s == 'e':
        if isr == True:
            finalString+='$'
        else:
            isr = True
            finalString+=s
    
    else:
        finalString+=s

print(finalString)