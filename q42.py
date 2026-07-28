def running_max(nums):
    result = []
    maximum = nums[0]

    for num in nums:
        if num > maximum:
            maximum = num
        result.append(maximum)

    return result

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Running Maximum:", running_max(nums))