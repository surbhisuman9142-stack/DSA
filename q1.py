def parity(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

n = int(input("Enter a number: "))
print(parity(n))-