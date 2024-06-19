def sum_list():
    mylist1 = input("Enter the values of the list separated by space: ")
    mylist1 = list(map(int, mylist1.split()))
    sum1 =0
    for num in mylist1:
        sum1 += num
    print("The sum of the numbers in the list is: ",sum1)

sum_list()
