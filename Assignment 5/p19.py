# 19.Write a Python program to find smallest and largest word in a given string.
#i/p=My name is not what you think it is
#o/p=Smallest word: My,Largest word: think
string = input("enter the string : ")  
word = ""  
words = []  
string = string + " "  

for i in range(0, len(string)):    
    if(string[i] != ' '):  
        word = word + string[i]  
    else:    
        words.append(word) 
        word = ""
small = large = words[0]  
for k in range(0, len(words)):    
    if(len(small) > len(words[k])):  
        small = words[k]  
    if(len(large) < len(words[k])):  
        large = words[k]
print("Smallest word: " + small)  
print("Largest word: " + large)