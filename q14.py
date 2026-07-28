<<<<<<< HEAD
def prime(n):
    if n < 2:
        return False
    i = 2
    while i*i<=n:
        if n%i == 0:
            return False
        i += 1
    return True
n = int(input('Enter number:'))
=======
def prime(n):
    if n < 2:
        return False
    i = 2
    while i*i<=n:
        if n%i == 0:
            return False
        i += 1
    return True
n = int(input('Enter number:'))
>>>>>>> 596cfe7ab6357109cb8fa940fb993f33a597e2e5
print (prime(n))   