def fizzbuzz(n):
   return[
      "fizzbuzz" if i % 15 == 0
      else "fizz" if i % 3 == 0
      else "buzz" if i % 5 == 0
      else str(i)
      for i in range (1,n+1)
   ]
n = int(input("Enter any number:"))
print (fizzbuzz(n))