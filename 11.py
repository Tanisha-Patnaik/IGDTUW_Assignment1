def fibonacci(nb):
    fib_seq = [0, 1]
    while len(fib_seq) < nb:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:nb]
num2 = int(input("Enter first n number: "))
print("The fibonacci sequence of n number is: " + str(fibonacci(num2)))
