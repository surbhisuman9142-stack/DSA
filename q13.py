def count_vowels(s):
    vowels = set('aeiou')
    return sum(1 for ch in s if ch in vowels)
text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))
