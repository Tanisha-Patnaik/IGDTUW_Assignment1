def char_freq(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


str7 = input("Enter the string: ")
print(char_freq(str7))