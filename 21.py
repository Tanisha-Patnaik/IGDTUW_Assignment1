def count_occurences():
    list2 = input("Enter the values of the list separated by space: ")
    list2 = list(map(int, list2.split()))
    elem = int(input("Enter the element from the list to find its number of occurrences: "))
    print(f"The occurrence of {elem} in the list is: ",list2.count(elem))

count_occurences()