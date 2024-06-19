def sum1(n):
    sum_1 = 0
    for digit in str(n):
        sum_1 += int(digit)
    return sum_1


num1 = int(input("Enter any number: "))
print("The sum of the digits is: " + str(sum1(num1)))