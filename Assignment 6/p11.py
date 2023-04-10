# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
result=int(input("what marks do you have?"))
if result>80:
    print("A grade achived ")
elif 80>result and result>60:
    print("B grade achived")
elif 60>result and result<50:
    print("C grade achieved")
elif 50>result and result<45:
    print("D grade achieved")
elif 45>result and result<25:
    print("E grade achieved")