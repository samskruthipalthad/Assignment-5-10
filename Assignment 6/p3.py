a = int(input("enter the number \n"))
print(type(a))
if a % 3 == 0 and  a % 5 == 0:
    print("fizzbuzz")
elif a % 5 == 0:
    print("buzz")
elif a % 3 == 0:
    print("fizz")
else:
    print("invalid number")