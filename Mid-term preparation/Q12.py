def get_no2(nums):
    nums.remove(max(nums))
    return max(nums)
print(get_no2([0, 1, 5, 4, 3]))