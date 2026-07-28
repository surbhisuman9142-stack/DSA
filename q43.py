def sum_array(arr):
    total = 0

    for i in range(len(arr)):
        total = total + arr[i]

    return total


# Input
n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    arr.append(num)

# Output
result = sum_array(arr)
print("Sum of array =", result)