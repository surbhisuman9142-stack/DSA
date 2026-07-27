from collections import Counter
def first_unique(xs):
    c = Counter(xs)
    for x in xs:
        if c[x] == 1:return x
    return None
numbers = [4,5,1,2,1,2,4]
result = first_unique(numbers)
print(result)