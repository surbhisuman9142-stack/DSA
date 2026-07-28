from collections import Counter
def word_freq(text):
    return dict(Counter(text.lower().split()))
text = input("Enter a sentence:")
print(word_freq(text))