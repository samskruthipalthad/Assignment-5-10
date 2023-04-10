# Write a Python program to check a triangle is equilateral, isosceles or scalene.
#Input lengths of the triangle sides: 
#x: 2,y: 2,z: 9
#isosceles triangle
print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("Equilateral triangle")
elif x==y or y==z or z==x:
    print("isosceles triangle")
else:
    print("Scalene triangle")