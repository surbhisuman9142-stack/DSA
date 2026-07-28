<<<<<<< HEAD
def reverse_int(n):
    rev = 0
    while n>0:
        rev = rev*10+n%10
        n//=10
    return rev
n = int(input("Enter number:"))
=======
def reverse_int(n):
    rev = 0
    while n>0:
        rev = rev*10+n%10
        n//=10
    return rev
n = int(input("Enter number:"))
>>>>>>> 596cfe7ab6357109cb8fa940fb993f33a597e2e5
print(reverse_int(n))