#3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
# Sample String : 'loseyourselfinthemovement'
# Expected Result : 'lont”'
# Sample String : 'sa'
# Expected Result : 'sasa'
# Sample String : 'f'
# Expected Result : Empty String 

str = input('Enter the string:\n')
string_len = len(str)
if(string_len < 2):
    print('Empty String')
else:
    op_str = str[0]+str[1]+str[string_len-2]+str[string_len-1]
    print(op_str)