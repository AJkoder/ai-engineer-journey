# HeartTalk - Exception Handling

try:
    number = int(input("Enter a number: "))

    if number < 0:
        raise ValueError("Negative numbers are not allowed.")

    result = 100 / number

except ValueError as error:
    print(f"Invalid input: {error}")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print(f"100 divided by {number} is {result}.")

finally:
    print("Thank you for using HeartTalk!")