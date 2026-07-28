def single_number(xs):
    r = 0
    for x in xs: r ^= x
    return r
xs = [4,3,3,5,5]
print(single_number(xs))