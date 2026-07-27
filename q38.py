from collections import Counter
def top_k(xs,k):
    return[value for value, _ in Counter(xs).most_common(k)]
numbers = [1,1,1,2,2,3]
k = 2
print(top_k(numbers,k))
