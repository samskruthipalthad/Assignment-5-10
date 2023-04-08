# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)
#sam,beauty,her,sam,love,her
#beauty,her,love,sam
items = input("Input comma separated sequence of words:\n")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))