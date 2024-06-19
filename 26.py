def check_prefix_suffix(string,prefix,suffix):
    return string.startswith(prefix) and string.endswith(suffix)

string1 = input("Enter a string: ")
prefix1 = input("Enter the prefix word for checking: ")
suffix1 = input("Enter the suffix word for checking: ")
print(check_prefix_suffix(string1,prefix1,suffix1))
