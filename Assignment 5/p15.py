# Write a Python program to count repeated characters in a string.
def char_frequency(input):
    char_dict={}
    for char in input:
        if char in char_dict:
            char_dict[char]+=1
        else:
            char_dict[char]=1
    most_frequent = max(char_dict,key=char_dict.get)
    return most_frequent,char_dict.get(most_frequent)

print(char_frequency("google.com"))
