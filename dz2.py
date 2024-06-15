chose = int(input("Enter num (1-7) "))
match chose:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednsday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("There are only 7 days in week")

month = int(input("Enter your num (1-12) "))
match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("There are only 12 month in a year")

num = int(input("enter your num: "))
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is equal to zero")

num_1 = int(input("Enter your first num: "))
num_2 = int(input("Enter your second num: "))
if num_1 == num_2:
    print("Numbers are equal")
elif num_1 > num_2:
    print(num_2, num_1)
else:
    print(num_1, num_2)
