def calculator(num1 , num2 , operator):
    if operator == "+" :
        return num1 + num2
    elif operator == "-" :
        return num1 - num2
    elif operator == "*" :
        return num1 * num2
    elif operator == "/" and num2 != 0:
        return num1 / num2
    else:
        return "choose appropriate operator from the list."

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
print("For addition choose: '+'\nFor subtraction choose: '-'\nFor multiplication choose: '*'\nFor division choose: '/'")
operator1 = input("Enter the operation you want to do: ")

print("The result is: ",calculator(number1,number2,operator1))
