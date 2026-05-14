try:
    num=int(input("Enter a number not equal to zero: "))
    print(10/num)
except ZeroDivisionError as err:
    print("The number is zero")
except ValueError:
    print("The input is not a number")
except :
    print("some error")