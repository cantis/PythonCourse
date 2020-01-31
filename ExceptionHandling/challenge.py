""" 173 Challenge """
FIRST = input("First Number: ")
SECOND = input("Second Number: ")

try:
    RESULT = int(FIRST) // int(SECOND)
    print(f"Result of {FIRST} devided by {SECOND} is {RESULT}")
except ValueError:
    #handle convert from string to int error TODO Remove this
    print("Please enter an integer.")
except ZeroDivisionError:
    print("You can't devide by zero")
