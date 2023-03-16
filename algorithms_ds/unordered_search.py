# My solution pre-teaching
def binary_find_int(nums: list, to_find: int) -> int:
    '''
    arguments: list of numbers
    returns: position of element searched for in the list. returns -1 if not found
    binary find int uses binary search to look for a specific value and returns the position of the value if found
    '''
    # Get halfway index
    half_incrementer = int(len(nums) / 2)
    for i in range(len(nums) - 1):
        if i == half_incrementer:
            return -1
        elif nums[i] == to_find:
            return i
        elif half_incrementer == len(nums):
            return -1
        elif nums[half_incrementer] == to_find:
            return half_incrementer
        half_incrementer += 1

nums = [1, 10, 22, 982]
nums2 = [11, 109, 222, 9821, 21, 99, 88]

print(binary_find_int(nums, 22))
print(binary_find_int(nums2, 88))
print(binary_find_int(nums2, 881))