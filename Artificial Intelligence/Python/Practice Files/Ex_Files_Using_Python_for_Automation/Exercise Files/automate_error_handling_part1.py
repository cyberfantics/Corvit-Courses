try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("The result is:",result)
except ValueError:
    print("You must enter a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")