num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))
chose = int(input("Choose what to do:\n1)Find sum of numbers\n2)Find product of numbers"))
match chose:
    case 1:
        print(f"Sum of numbers + {num_1 + num_2 + num_3}")
    case 2:
        print(f"Product of numbers + {num_1 * num_2 * num_3}")

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))
chose = int(input("Choose what to do:\n1)Find max number\n2)Find min number\n3) Find AR"))
match chose:
    case 1:
        if num_1 > num_2 and num_1 > num_3:
            print(num_1)
        elif num_2 > num_1 and num_2 > num_3:
            print(num_2)
        elif num_3 > num_1 and num_3 > num_2:
            print(num_3)
        else:
            print("Numbers are equal")
    case 2:
        if num_1 < num_2 and num_1 < num_3:
            print(num_1)
        elif num_2 < num_1 and num_2 < num_3:
            print(num_2)
        elif num_3 < num_1 and num_3 < num_2:
            print(num_3)
        else:
            print("Numbers are equal")
    case 3:
        print(f"AR = {(num_1 + num_2 + num_3)/3}")

metres = int(input("Enter metres: "))
chose = int(input("Choose what to do:\n1)Convert into miles\n2)Convert into inches\n3) Convert into yards\n"))
match chose:
    case 1:
        print(f"Miles = {metres // 1609}")
    case 2:
        print(f"Inches = {metres * 39.37}")
    case 3:
        print(f"Yards = {metres * 1.09361}")