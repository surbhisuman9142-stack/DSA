def count_even(nums):
    return sum(1 for x in nums if x % 2 == 0 )
nums  = [2,5,6,7,8]
print(count_even(nums))
