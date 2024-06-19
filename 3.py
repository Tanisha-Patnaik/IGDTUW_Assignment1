d = int((input("Enter a number: ")))
factorial = 1
if d < 0:
    print("Factorial does not exist.")
elif d == 0 or d == 1:
    print("Factorial is 1.")
else:
    for i in range(1, d + 1):
        factorial = factorial * i
print("The factorial of " + str(d) + " is " + str(factorial))
