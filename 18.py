def anagram(s1, s2):
    return sorted(s1) == sorted(s2)


str9 = input("Enter a word: ")
str10 = input("Enter another word to check anagram: ")
print(anagram(str9, str10))