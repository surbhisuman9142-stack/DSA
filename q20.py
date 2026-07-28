<<<<<<< HEAD
n = int(input("Enter any number:"))
while n>=10:
    s = 0
    while n > 0:
        s+=n%10
        n//=10
    n = s
=======
n = int(input("Enter any number:"))
while n>=10:
    s = 0
    while n > 0:
        s+=n%10
        n//=10
    n = s
>>>>>>> 596cfe7ab6357109cb8fa940fb993f33a597e2e5
print("single digit:",n)