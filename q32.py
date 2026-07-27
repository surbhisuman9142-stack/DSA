from collections import Counter
def most_frequent(xs):
    return Counter(xs).most_common(1)[0][0]
xs = [5,5,5,6,7,8]
print(most_frequent(xs))