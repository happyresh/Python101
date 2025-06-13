side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))

if (side1 == side2) and (side1 == side3):
    print("Equilateral")
elif (side1 == side2) or (side2 == side3) or (side1 == side3):
    print("Isosceles")
elif (side1 != side2) and (side2 != side3) and (side1 != side3):
    print("Scalene")
