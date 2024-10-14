def sum(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum(nums[1:])

print(sum([1, 2, 3, 4, 5]))
# 15
