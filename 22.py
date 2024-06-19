def find_max_min():
    list3 = input("Enter the values of the list separated by space: ")
    list3 = list(map(int, list3.split()))
    print("Minimum value from the string is: ", min(list3))
    print("Maximum value from the string is: ", max(list3))

find_max_min()