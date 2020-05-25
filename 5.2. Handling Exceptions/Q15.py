def get_no1(nums):
    nums.remove(max(nums))
    return max(nums)
in_list = [1,2,3,4, 5, 6]
print(get_no1(in_list))